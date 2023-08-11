from constants import *
import requests
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime, timedelta


token_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
}

reserve_libcal_space_params = {
    "start" : "2023-08-10T22:00:00+00:00",
    "test" : 1,

    "bookings": [{
    # 18451 - Student Centre, Group Study Room 2.17
    "id": 18451,
    "to": "2023-08-10T23:00:00+00:00",
    }]
}

# keep everything in ISO 8601 format?

print(datetime.now())
start_time = datetime(2023, 8, 12, 9, 18, 10)
execution_time = start_time - timedelta(days=3)
print(execution_time)


# Is this code dodgy?
def book_study_space():
    r = requests.post("https://uclapi.com/libcal/space/reserve", json=reserve_libcal_space_params, params=token_params)
    print(r.status_code)
    print(r.json())

    global FLAG
    FLAG = False

FLAG = True
sch = BackgroundScheduler()
sch.add_job(book_study_space, 'date', run_date=execution_time)
sch.start()

while FLAG:
    pass
quit()

# async request 
# javascript built in request
# jquery 
# try in boostrap


# store request in database

# use sql alchemy - handle multiple requests 
# multithreading 

# store token in browser cache 

# user ids 
# requests table 

# flask session management - know who the request if from 

