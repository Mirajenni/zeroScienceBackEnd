from flask import Flask
from satelliteLocation import SatelliteLocation
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

satellite = {}
satellite_list = [{}]

sl = SatelliteLocation()

app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

@app.route('/')
def index():
    return 'Página Login'

@cross_origin()
@app.route('/getSatellitesFile')
def prepare_sat():
    fname = "test_list.txt"
    data = sl.get_all(fname, debug=True)
    return json.dumps(data)

@cross_origin()
@app.route('/getSatellitesNear')
def prepare_near():
    data = sl.get_near(debug = True)
    for i in data:
        del i["info"]
        for j in i['above']:
            del j["intDesignator"]
    return json.dumps(data)

if __name__ == '__main__':
    app.run(host= '0.0.0.0')
