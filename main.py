import requests
from constants import *
from flask import Flask, request, render_template
from store_booking_in_database import store_booking_in_database
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def home_2():
    return render_template("index.html")


# Callback url which handles the OAuth
@app.route("/callback")
def recieve_callback():
    # receive parameters
    RESULT = request.args.get('result', '')
    STATE = request.args.get('state', '')
    CLIENT_ID = request.args.get('client_id' '')
    CODE = request.args.get('code', '')

    # Request auth token from /oauth/token
    get_token_params = {
        "code" : CODE,
        "client_id" : CLIENT_ID,
        "client_secret" : CLIENT_SECRET
    }

    r = requests.get("https://uclapi.com/oauth/token", params=get_token_params)
    # print(r.json())
    ACCESS_TOKEN = r.json()['token']


    # Store Access Token in constants.py | Needs to be moved to JSON or database
    with open("constants.py", "a") as f:
        f.write(f'\nACCESS_TOKEN = "{ACCESS_TOKEN}"')

    # Redirect user to the signed in home page
    return render_template("signed_in.html")


@app.route("/signed_in.html")
def signed_in():
    return render_template("signed_in.html")


@app.route("/book_space.html")
def book_space():
    return render_template("book_space.html")


@app.route("/my_bookings.html")
def my_bookings():
    return render_template("my_bookings.html")


# Form from book_space.html sent here ( <form action="/process_booking" method="post"> )
@app.route("/my_bookings.html", methods=["POST"])
def process_booking():
    room_number = request.form['room-number']
    date = request.form['selected-date']
    start_time = request.form['start-time']
    end_time = request.form['end-time']

    # Get the time the booking request is made, which is the current time right now
    request_made_time = datetime.now().isoformat(' ', 'seconds')

    # Lookup table to convert room number into room id | Need to move this to database and expand options
    room_num_to_id = { "2.02":18444, "2.03":18445, "2.05":18446, "2.10":18447, "2.12":18448, "2.13":18449, "2.15":19225,
                        "2.16" : 18450, "2.17" : 18451 }
    room_id = room_num_to_id[room_number]
    
    # Store booking in bookings.db database
    store_booking_in_database(room_number, room_id, date, start_time, end_time, request_made_time)

    return render_template("my_bookings.html")

# separate process - reads the database and books
# separate thread - continously checks the database and makes booking
# Search: How to create a thread in Python 


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
