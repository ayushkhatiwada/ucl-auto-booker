from constants import *
import requests
import json


get_all_libcal_locations_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
    "details" : 0
}

r = requests.get("https://uclapi.com/libcal/space/locations", params=get_all_libcal_locations_params)
print(r.status_code)

with open('json_files/1_all_libcal_locations.json', 'w') as f:
    json.dump(r.json(), f)
