from flask import Flask, render_template, request
from math import radians, sin, cos, atan2, sqrt, degrees

import json
import os
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    creds = [os.environ.get('HERE_APP_ID'), os.environ.get('HERE_APP_CODE')]

    return render_template("index.html", creds=creds)

@app.route("/calcmiddle", methods=['POST'])
def calcmiddle():
    app_id = os.environ.get('HERE_APP_ID')
    app_code = os.environ.get('HERE_APP_CODE')

    addresses = [request.form['addr1'], request.form['addr2']]
    coords = []

    for addr in addresses:
        payload = {'app_id': app_id, 'app_code': app_code, 'searchtext': addr}
        r = requests.get('https://geocoder.api.here.com/6.2/geocode.json', params=payload)

        data = r.json()

        lat = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Latitude']
        lon = data['Response']['View'][0]['Result'][0]['Location']['DisplayPosition']['Longitude']

        coords.append(lat)
        coords.append(lon)
    
    # calculate the halfway lat lon
    lat1, lon1, lat2, lon2 = map(radians, coords)
    bx = cos(lat2) * cos(lon2 - lon1)
    by = cos(lat2) * sin(lon2 - lon1)
    lat3 = atan2(sin(lat1) + sin(lat2), sqrt((cos(lat1) + bx) * (cos(lat1) + bx) + by**2))
    lon3 = lon1 + atan2(by, cos(lat1) + bx)
    
    mid = {'Latitude': degrees(lat3), 'Longitude': degrees(lon3)}
    pins = getpins(mid)

    ret = {'coords': mid, 'pins': pins}

    return json.dumps(ret)

def getpins(mid):
    app_id = os.environ.get('HERE_APP_ID')
    app_code = os.environ.get('HERE_APP_CODE')

    at = str(mid['Latitude']) + ',' + str(mid['Longitude'])
    
    payload = {'app_id': app_id, 'app_code': app_code, 'at': at, 'cat': 'eat-drink'}

    r = requests.get('https://places.api.here.com/places/v1/discover/explore', params=payload)
    data = r.json()

    return data




