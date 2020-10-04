from flask import Flask
import satelliteLocation as sl
import json

app = Flask(__name__)

@app.route('/')
def index():
    return 'Página Login'

satellite_list = []
class Satellite:
    def __init__(self, id, name, lat, lon, alt):
        self.id = id
        self.name = name
        self.lat = lat
        self.lon = lon
        self.alt = alt

@app.route('/getSatellitesFile')
def prepare_sat():
    fname = "test_list.txt"
    data = sl.get_all(fname, debug=True)
    for i in data:
        print("\n")
        sat_id = i['info']['satid']
        sat_name = i['info']['satname']
        for j in i['positions']:
            sat_lat = j['satlatitude']
            sat_lon = j['satlongitude']
            sat_alt = j['sataltitude']
        d = Satellite(sat_id, sat_name, sat_lat, sat_lon, sat_alt)
        satellite_list.append(d)

    '''for i in satellite_list:
        print("Lista {} {} {} {} {}\n".format(i.id, i.name, i.lat, i.lon, i.alt))'''

    return json.dumps(data)


''' print("ID: {}, Nome: {}, Latitude: {}, Longitude: {}, Altitude: {}" .format
    (data[0]['info']['satid'], 
    data[0]['info']['satname'],
    data[0]['positions'][0]['satlatitude'],
    data[0]['positions'][0]['satlongitude'],
    data[0]['positions'][0]['sataltitude']))'''
