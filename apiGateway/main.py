#!/usr/bin/python3

from flask import Flask, request, jsonify
import requests
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
BACKEND_SERVICES = {
    'site': 'http://127.0.0.1:8000',
}

@app.route('/api/<service>', methods=['GET', 'POST'])
def route_requests(service):

    #tmp
    print(request.get_data())
    print(service)
   
    if service in BACKEND_SERVICES:
        backend_url = BACKEND_SERVICES[service]
        forward_url = f"{backend_url}{request.path}"
        headers = dict(request.headers)
        response = requests.request(
            method=request.method,
            url=forward_url,
            headers=headers,
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )
        print(response)
        print(response.json())
        return jsonify(response.json()), response.status_code, response.headers.items()
    else:
        return jsonify({'error': f'Service {service} not found'}, 404)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

