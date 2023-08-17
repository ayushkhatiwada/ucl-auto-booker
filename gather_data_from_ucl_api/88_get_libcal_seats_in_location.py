# Get all LibCal seats in a given location
from constants import *
import requests
import json

params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,

    # # (string) ids - A single LibCal location ID
    # # 872 - Student Centre location ID
    "ids" : "872",
    # "category_id" : "5429"
}

r = requests.get("https://uclapi.com/libcal/space/seats", params=params)
print(r.status_code)

with open('../88_all_libcal_seats_in_location.json', 'w') as f:
    json.dump(r.json(), f, indent=2)

