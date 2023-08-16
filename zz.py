from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from dateutil import parser as date_parser

def my_function():
    print("Function executed at:", datetime.now())

scheduler = BackgroundScheduler()

# Replace this ISO 8601 datetime string with your specific date and time
iso_8601_datetime = "2023-08-18T18:30:00+00:00"
parsed_datetime = date_parser.parse(iso_8601_datetime)

# Calculate the time exactly 3 days before the given datetime
new_datetime = parsed_datetime - timedelta(days=3)

scheduler.add_job(my_function, run_date=new_datetime)

scheduler.start()

# Keep the script running
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
