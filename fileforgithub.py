from flask import Flask, render_template, request
import requests
import os
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './temp/'

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    # get form data
    api_token = request.form['api_token']
    username = request.form['username']
    reponame = request.form['reponame']
    filepath = request.form['filepath']
    file = request.files['file']
    
    # save file to temp directory
    filename = file.filename
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # read file from temp directory and encode in base64
    with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as f:
        content = f.read()
        content_b64 = base64.b64encode(content).decode()

    # make API request to create or update file on GitHub
    url = f'https://api.github.com/repos/{username}/{reponame}/contents/{filepath}'
    headers = {'Authorization': f'token {api_token}'}
    data = {
        'message': 'uploading file',
        'content': content_b64
    }
    response = requests.put(url=url, headers=headers, json=data)

    # delete file from temp directory
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    if response.ok:
        raw_url = response.json()['content']['download_url']
        return f'File uploaded successfully. Raw URL: {raw_url}'
    else:
        return f'Error uploading file: {response.text}'

if __name__ == '__main__':
    app.run(debug=True)
