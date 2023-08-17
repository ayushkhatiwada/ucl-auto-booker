# Better Design for this? JSON? Database? - Probably best if JSON
LOGIN_URL = "https://uclapi.com/oauth/authorise/?client_id=3574900202627382.9436735244241114&state=ayush"

# Table 1 - sql lite
CLIENT_ID = "3574900202627382.9436735244241114"
CLIENT_SECRET = "0d315d216e649e473a84f5373cf47688c0ff78833fc7f1aed6a0ddd9fe6862d0"

# Table 2: access_token + session id + timestamp (note token may expire)
ACCESS_TOKEN = "uclapi-user-c25a0d0716a5c58-7ce172116b77662-7111bdf5521fbdc-36ba40f8f148b0f"

# Table 3: Booking to made - state flag (pending, failed, succeeded) - store times for each state
## maybe not have in progress


# store in SQLite / database

# possibly store session ID + timestamp
# store acces_token in booking database


# two threads - one to get bookings and write to database
# - 2nd thread to read bookings and make bookings
# 2nd thread wakes up when it is time to make a booking


# exponential back off algorithms 
ACCESS_TOKEN = "uclapi-user-c25a0d0716a5c58-7ce172116b77662-7111bdf5521fbdc-36ba40f8f148b0f"