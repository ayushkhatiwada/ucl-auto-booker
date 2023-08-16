import requests
from constants import *
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta


def excecute_booking(room_number, date, start_time, end_time):
    
    print(room_number, date, start_time, end_time)
    # 2.17 2023-08-18 14:00 15:00

    # Puts times into ISO 8601 format e.g "2023-08-10T22:00:00+00:00"
    start_time_iso_8601 = date + "T" + start_time + ":00+01:00"
    end_time_iso_8601 = date + "T" + end_time + ":00+01:00"
        ### Need to adjust time zone difference (+01:00) depending on whether it is GMT or BST


    # NEED lookup table to convert room number into space id
    room_to_id = { "2.17" : 18451 }
    room_id = room_to_id[room_number]

    token_params = {  
    "token" : ACCESS_TOKEN,
    "client_secret" : CLIENT_SECRET,
    }

    reserve_libcal_space_params = {
        "start" : start_time_iso_8601,
        "test" : 1,

        "bookings": [{
        "id": room_id,
        "to": end_time_iso_8601,
        }]
    }

    print(datetime.now())
    # Booking times open at 12:00 3 days before desired booking day
    # Booking made 2 seconds later to account for possible unsynchronised clocks (":02")
    execution_time_3_days_ahead = date + "T" + "12:00" + ":02+01:00"
    execution_time_3_days_ahead = datetime.fromisoformat(execution_time_3_days_ahead)
    execution_time = execution_time_3_days_ahead - timedelta(days=3)
    print("excecution time: ", execution_time)

    def book_study_space():
        r = requests.post("https://uclapi.com/libcal/space/reserve", json=reserve_libcal_space_params, params=token_params)
        print(r.status_code)
        print(r.json())

        global FLAG
        FLAG = False

    FLAG = True
    sch = BackgroundScheduler()
    sch.add_job(book_study_space, run_date=execution_time)
    sch.start()

    while FLAG:
        pass

    return 

### Note function needs to differentiate between bookings that can currently me made, and so it is booked straight away, 
# and bookings that need to be made in the future so 