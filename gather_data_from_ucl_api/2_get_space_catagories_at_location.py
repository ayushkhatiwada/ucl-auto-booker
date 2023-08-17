# Returns the categories of spaces available in the given location(s)
from constants import *
import requests
import json

params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,

    # (string) ids -  list of LibCal locations IDs separated by commas 
    # 872 - location ID of student centre
    "ids" : "872"
}

r = requests.get("https://uclapi.com/libcal/space/categories", params=params)
print(r.status_code)

with open('../data_from_ucl_api/2_space_catagories_at_location.json', 'w') as f:
    json.dump(r.json(), f, indent=2)
