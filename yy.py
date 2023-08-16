from constants import *
import requests
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime


token_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
}

reserve_libcal_space_params = {
    "start" : "2023-08-13T22:00:00+00:00",

    "test" : 1,
    
    "bookings": [{
    # 18451 - Student Centre, Group Study Room 2.17
    "id": 18451,
    "to": "2023-08-13T23:00:00+00:00",
    }]
}


print(datetime.now())
execution_time = datetime(2023, 8, 16, 12, 16, 10)
print(execution_time)


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
