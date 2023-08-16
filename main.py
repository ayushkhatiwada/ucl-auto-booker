import requests
from constants import *
from flask import Flask, request, render_template
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

    # NEED lookup table to convert room number into room id
    room_to_id = { "2.17" : 18451 }
    room_id = room_to_id[room_number]
    
    
    print("booking done")
    return render_template("book_space.html")

# separate process - reads the database and books
# execute_booking should store the booking in a datbase
# separate thread - continously checks the database and makes booking
# Search: How to create a thread in Python 


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)

