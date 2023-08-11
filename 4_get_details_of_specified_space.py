# Get details of all spaces specified by their sapce id
from constants import *
import requests
import json

params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,

    # (string) ids - Comma delimited list of LibCal space IDs
    # 18451 - Space ID of "Group Study Room 2.17"
    "ids" : 18446
}

r = requests.get("https://uclapi.com/libcal/space/item", params=params)
print(r.status_code)
print(r.json())

with open('json_files/4_details_of_specified_space.json', 'w') as f:
    json.dump(r.json(), f, indent=2)

