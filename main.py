import requests
from constants import *
from flask import Flask, request, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from execute_booking import excecute_booking
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/index.html")
def home_2():
    return render_template("index.html")


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


# Form from book_space.html sent here ( <form action="/process_booking" method="post"> )
@app.route("/process_booking", methods=["POST"])
def process_booking():
    room_number = request.form['room-number']
    date = request.form['selected-date']
    start_time = request.form['start-time']
    end_time = request.form['end-time']

    excecute_booking(room_number, date, start_time, end_time)
    
    return render_template("book_space.html")

if __name__ == "__main__":
    app.run(debug=True)
