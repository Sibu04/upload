from flask import Flask, render_template, request, redirect, url_for
import requests
import os
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './temp/'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # limit file size to 100 MB

@app.route('/')
def home():
    return render_template('upload.html')
    
@app.route('/upload', methods=['POST'])
def upload():
    # get form data
    api_token = request.form['api_token']
    username = request.form['username']
    reponame = request.form['reponame']
    filepath = request.form.get('filepath', None)
    file = request.files['file']

    # check if file size is within limit
    file_size = len(file.read())
    file.seek(0)
    if file_size > app.config['MAX_CONTENT_LENGTH']:
        return f'Error uploading file: file size exceeds limit of {app.config["MAX_CONTENT_LENGTH"]} bytes'
    # if filepath is not provided, use filename as filepath
    if not filepath:
        filepath = file.filename
    
    # check if file already exists in the specified path
    url = f'https://api.github.com/repos/{username}/{reponame}/contents/{filepath}'
    headers = {'Authorization': f'token {api_token}'}
    response = requests.get(url=url, headers=headers)

    if response.ok:
        # file already exists, rename file
        filename, extension = os.path.splitext(file.filename)
        count = 1
        new_filename = f"{filename}_{count}{extension}"
        while requests.get(f"https://api.github.com/repos/{username}/{reponame}/contents/{new_filename}", headers=headers).ok:
            count += 1
            new_filename = f"{filename}_{count}{extension}"
        filepath = new_filename
        message = f'File already exists, renamed file to {filepath}'
    else:
        message = 'Uploading file'

    # save file to temp directory
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filepath))

    # read file from temp directory and encode in base64
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filepath), 'rb') as f:
        content = f.read()
        content_b64 = base64.b64encode(content).decode()

    # make API request to create or update file on GitHub
    url = f'https://api.github.com/repos/{username}/{reponame}/contents/{filepath}'
    data = {
        'message': message,
        'content': content_b64
    }
    response = requests.put(url=url, headers=headers, json=data)

    # delete file from temp directory
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filepath))

    if response.ok:
        raw_url = response.json()['content']['download_url']
        return redirect(url_for('response', url=raw_url))
    else:
        return f'Error uploading file: {response.text}'

@app.route('/response')
def response():
    url = request.args.get('url')
    return render_template('response.html', url=url)
    
if __name__ == '__main__':
    app.run(debug=True)
