API_KEY = "6GESWN-ABKBH6-CFMN7U-4KDO"

import requests
import toml
from pprint import pprint
from sys import argv, exit
from os import path

'''BASE_URL = "https://www.n2yo.com/rest/v1/satellite/"
TEMPLATE = "visualpasses/{id:d}/{observer_lat:.5f}/{observer_lng:.5f}/{observer_alt:2f}/{days:d}/{min_visibility:d}"'''

'''def retrieve_data(QUERY_URL, debug=False):
    "Retrieve data from given URL."
    if debug:
        print("Requesting data from: {}".format(QUERY_URL))
    r = requests.get(QUERY_URL, params={"apiKey" : API_KEY})
    if r.status_code == requests.codes.ok:
        if debug:
            print("Success.")
        return r.json()
    elif debug:
        print("Failed! (status code {})".format(r.status_code))
    return "{}"'''

#Para REQUEST DE SATELITES EM LATITUDE E LONGITUDE TAL
URL = "https://www.n2yo.com/rest/v1/satellite/positions/20580/-8.053/-34.881/74.042/15/&apiKey=6GESWN-ABKBH6-CFMN7U-4KDO"
#LOCATION = "positions/{id:d}/{observer_lat:.5f}/{observer_lng:.5f}/{observer_alt:2f}/2/&{api:API_KEY}"


def retrieve_data():
    print("Requesting data from: {}".format(URL))
    r = requests.get(URL)
    if r.status_code == requests.codes.ok:
        print("Success.")
        print(r.text)
        return r.json()
    elif debug:
        print("Failed! (status code {})".format(r.status_code))
        return "{}"
    
    
if __name__=="__main__":
    retrieve_data()
