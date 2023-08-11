from constants import *
import requests
import json


get_libcal_bookings_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
    "eid" : 18451
}

r = requests.get("https://uclapi.com/libcal/space/bookings", params=get_libcal_bookings_params)
print(r.status_code)

with open('json_files/libcal_bookings.json', 'w') as f:
    json.dump(r.json(), f)
