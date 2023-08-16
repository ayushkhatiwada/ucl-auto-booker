from constants import *
import requests
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime, timedelta


token_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
}

reserve_libcal_space_params = {
    "start" : "2023-08-18T22:00:00+00:00",
    "test" : 1,

    "bookings": [{
    # 18451 - Student Centre, Group Study Room 2.17
    "id": 18451,
    "to": "2023-08-18T23:00:00+00:00",
    }]
}

# keep everything in ISO 8601 format?

print("current time: ", datetime.now())
test_time = "2023-08-18T22:06:00+00:00"
year = int(test_time[0:4])
month = int(test_time[5:7])
day = int(test_time[8:10])
hour = int(test_time[11:13])
minute = int(test_time[14:16])

start_time = datetime(year, month, day, hour, minute, 0)
execution_time = start_time - timedelta(days=3)
print("excecution time: ", execution_time)


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


