import json
import requests
from flask import Flask, request, Response
from uvicorn import run

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    json_url = request.args.get('json_url')
    start = request.args.get('start')
    end = request.args.get('end')
    limit = request.args.get('limit')

    response = requests.get(json_url)
    json_data = json.loads(response.text)

    if start:
        start = int(start)
    else:
        start = 0

    if end:
        end = int(end)
    else:
        end = len(json_data)

    if limit:
        limit = int(limit)
        end = start + limit

    response_data = json_data[start:end]
    response = Response(json.dumps(response_data), mimetype='application/json')
    return response

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8000)
