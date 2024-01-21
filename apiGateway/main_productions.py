#!/usr/bin/python3

from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import logging
import time 

logging.basicConfig(filename='all.log', encoding='utf-8', level=logging.DEBUG)
def log(request, service):
    logging.info(f'{time.time} -> {request.method} -> {service}')

app = Flask(__name__)
CORS(app)

# 64.225.80.227
BACKEND_SERVICES = {
    'site': 'http://64.225.80.227',
    'getSites': 'http://64.225.80.227',
    'articles': 'http://159.223.243.81',
    'runSite': 'http://64.225.80.227',
    'deleteSite': 'http://64.225.80.227',
    'user': 'http://64.225.80.227',
}

@app.route('/api/<service>/<path:subpath>', methods=['GET', 'POST'])
@app.route('/api/<service>', methods=['GET', 'POST'])
def route_requests(service, subpath=None):
    try:
        if service in BACKEND_SERVICES:
            print("inside service")
            backend_url = BACKEND_SERVICES[service]
            forward_url = f"{backend_url}{request.path}"
            print(forward_url)
            headers = dict(request.headers)
            response = requests.request(
                method=request.method,
                url=forward_url,
                headers=headers,
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False
            )

            return jsonify(response.json()), response.status_code, response.headers.items()
        else:
            print("Nope")
            return jsonify({'error': f'Service {service} not found'}, 404)
    except Exception as E:
        return jsonify({'error': 'Internal error'}, 500)
    
        
if __name__ == '__main__':
    app.run(debug=True, port=8080)

