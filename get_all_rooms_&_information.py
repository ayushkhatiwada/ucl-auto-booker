"""
ROOM BOOKINGS
Returns rooms and information about them.
GET /roombookings/rooms
If you don't specify any query parameters besides the token, all rooms will be returned.

Note: This endpoint only returns publicly bookable rooms. Departmentally bookable rooms are not included.
In the response, the room field contains a list of rooms that match your query. If no filters are applied,
all rooms will be returned. """

from constants import *
import requests
import json


get_room_bookings_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET
}

r = requests.get("https://uclapi.com/roombookings/rooms", params=get_room_bookings_params)
print(r.status_code)

with open('json_files/room_bookings.json', 'w') as f:
    json.dump(r.json(), f)
