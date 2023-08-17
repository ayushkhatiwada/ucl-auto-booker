# Gets all personal bookings made by user
from constants import *
import requests
import json


params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
}

r = requests.get("https://uclapi.com/libcal/space/personal_bookings", params=params)
print(r.status_code)

with open('../data_from_ucl_api/6_personal_bookings.json', 'w') as f:
    json.dump(r.json(), f, indent=2)

