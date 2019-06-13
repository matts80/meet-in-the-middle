from flask import Flask, render_template, request

import json
import os
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/calcmiddle", methods=['POST'])
def calcmiddle():
    app_id = os.environ.get('HERE_APP_ID')
    app_code = os.environ.get('HERE_APP_CODE')

    addresses = {'addr1': request.form['addr1'], 'addr2': request.form['addr2']}
    coords = {}

    for addr, value in addresses.items():
        payload = {'app_id': app_id, 'app_code': app_code, 'searchtext': value}
        r = requests.get('https://geocoder.api.here.com/6.2/geocode.json', params=payload)

        data = r.json()

        lat = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
        lon = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']

        coords[addr] = {'Latitude': lat, 'Longitude': lon}

    return json.dumps(coords)