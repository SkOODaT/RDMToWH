from flask import Flask, request
import requests, os
import urllib3

import pprint

app = Flask(__name__, static_url_path='')

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

WEBHOOK_URL_1 = "192.168.1.100:4000"
WEBHOOK_URL_2 = None
WEBHOOK_URL_3 = None
WEBHOOK_URL_4 = None
WEBHOOK_URL_5 = None

@app.route('/')
def homepage():
    return "Python RDMToWH Connector V1.1"

@app.route("/", methods=["POST"])
def raw():
    data = request.get_json(force=True)
    print("[RDMToWH] WEBHOOK DATA RECEVED")
    #pprint.pprint(data)
    #for info in data:
    #    print(info['type'])
    req = str()
    try:
        if WEBHOOK_URL_1 is not None:
            req = requests.post(url='http://'+WEBHOOK_URL_1+'/', json=data, timeout=1)
            print("[RDMToWH] WEBHOOK URL 1")
        if WEBHOOK_URL_2 is not None:
            req = requests.post(url='http://'+WEBHOOK_URL_2+'/', json=data, timeout=1)
            print("[RDMToWH] WEBHOOK URL 2")
        if WEBHOOK_URL_3 is not None:
            req = requests.post(url='http://'+WEBHOOK_URL_3+'/', json=data, timeout=1)
            print("[RDMToWH] WEBHOOK URL 3")
        if WEBHOOK_URL_4 is not None:
            req = requests.post(url='http://'+WEBHOOK_URL_4+'/', json=data, timeout=1)
            print("[RDMToWH] WEBHOOK URL 4")
        if WEBHOOK_URL_5 is not None:
            req = requests.post(url='http://'+WEBHOOK_URL_5+'/', json=data, timeout=1)
            print("[RDMToWH] WEBHOOK URL 5")
        if req.status_code not in [200,201]:
            print("[RDMToWH] Status code: {}".format(req.status_code))
    except urllib3.exceptions.ProtocolError as de:
        retry_error = True
        print("[RDMToWH] ERROR:", de)
    except requests.exceptions.ConnectionError as ce:
        retry_error = True
        print("[RDMToWH] ERROR:", ce)

    return 'OK'

if __name__ == "__main__":
    print('[RDMToWH] Python RDMToWH Connector V1.1')
    app.run(host="192.168.1.100", port=6060, debug=True)
