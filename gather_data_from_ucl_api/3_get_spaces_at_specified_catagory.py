# Get all spaces corresponding to the specified categories
from constants import *
import requests
import json

params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,

    # (string) ids -  Comma delimited list of LibCal category IDs
    # 5428 - Category ID of Group Study
    "ids" : "5428"
}

r = requests.get("https://uclapi.com/libcal/space/category", params=params)
print(r.status_code)

with open('../data_from_ucl_api/3_spaces_at_specified_catagory.json', 'w') as f:
    json.dump(r.json(), f, indent=2)

