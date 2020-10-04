from flask import Flask
import satelliteLocation as sl
import json

app = Flask(__name__)


satellite = {}
satellite_list = [{}]

@app.route('/')
def index():
    return 'Página Login'

@app.route('/getSatellitesFile')
def prepare_sat():
    fname = "test_list.txt"
    data = sl.get_all(fname, debug=True)
    return json.dumps(data)

@app.route('/getSatellitesNear')
def prepare_near():
    data = sl.get_near(debug = True)
    for i in data:
        del i["info"]
        for j in i['above']:
            del j["intDesignator"]


    #para acessar:
    #for i in data:
    #    for j in i['above']:
    #        print(j['satid'])

    return json.dumps(data)