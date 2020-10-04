from flask import Flask
import satelliteLocation as sl
import json

app = Flask(__name__)

satellite_list = []
class Satellite:
    def __init__(self, id, name, lat, lng, alt):
        self.id = id
        self.name = name
        self.lat = lat
        self.lng = lng
        self.alt = alt

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
        for j in i['above']:
            sat_id = j['satid']
            sat_name = j['satname']
            sat_lat = j['satlat']
            sat_lng = j['satlng']
            sat_alt = j['satalt'] 
            d = Satellite(sat_id, sat_name, sat_lat, sat_lng, sat_alt)
            satellite_list.append(d)

    #Para RECEBER
    #for i in satellite_list:
    #    print("{} {} {} {} {}\n".format(i.name, i.name, i.lat, i.lng, i.alt))

    return json.dumps(data)