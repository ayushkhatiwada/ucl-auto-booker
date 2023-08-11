import requests
from constants import *
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index.html")
def home_2():
    return render_template("index.html")

# @app.route("/login")
# def uclapi_login():
#     return redirect(url)

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
    print(r.json())
    ACCESS_TOKEN = r.json()['token']
    with open("constants.py", "a") as f:
        f.write(f'\nACCESS_TOKEN = "{ACCESS_TOKEN}"')
    print()

    # Redirect user to the signed in home page
    return render_template("signed_in.html")

@app.route("/signed_in.html")
def signed_in():
    return render_template("signed_in.html")

@app.route("/book_space.html")
def book_space():
    return render_template("book_space.html")



if __name__ == "__main__":
    app.run(debug=True)
