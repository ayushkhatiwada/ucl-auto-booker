from constants import *
import requests

token_params = {
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET
}

reserve_libcal_space_params = {

    "start": "2023-08-12T23:00:00+00:00",
    "test": 1,

    "bookings": [{
        "id": 18451,
        "to": "2023-08-12T23:30:00+00:00",
        }]
}

r = requests.post("https://uclapi.com/libcal/space/reserve", json=reserve_libcal_space_params, params=token_params)
print(r.status_code)
print(r.json())


