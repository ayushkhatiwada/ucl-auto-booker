from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Define the base class for declarative models
Base = declarative_base()

# Define the Booking class
class Booking(Base):

    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_id = Column("room_id", Integer)
    date = Column("date", String)
    start_time = Column("start_time", String)
    end_time = Column("end_time", String)

    def __init__(self, room_id, date, start_time, end_time):
        self.room_id = room_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time


# Create an engine and connect to the "bookings" database
engine = create_engine("sqlite:///bookings.db", echo=True)

# Create the "bookings" table in the database
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to create a new Booking instance and store it in the database
def store_booking_in_database(room_id, date, start_time, end_time):
    new_booking = Booking(room_id=room_id, date=date, start_time=start_time, end_time=end_time)
    session.add(new_booking)

    session.commit()
    session.close()

# booking0 = Booking(18451, "2023-08-19", "21:00", "22:00")
# session.add(booking0)

# # Commit the transaction to save the new_booking to the database + Close the session
# session.commit()
# session.close()

