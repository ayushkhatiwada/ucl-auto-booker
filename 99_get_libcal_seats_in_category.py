# Get all LibCal seats in a given category - I think?
from constants import *
import requests
import json

params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,

    # (string) ids - Comma delimited list of LibCal category IDs
    # Strange - gives error upon entering category ID
    "ids" : "1497",
}

r = requests.get("https://uclapi.com/libcal/space/seat", params=params)
print(r.status_code)

with open('json_files/99_all_libcal_seats_in_category.json', 'w') as f:
    json.dump(r.json(), f)

