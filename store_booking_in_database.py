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
    status = Column("status", String)
    """
    Status of booking. Could be:
    1. Pending - Book has not been made. Waiting for bookable window to open to execute booking 
    2. Completed - Booking completed
    Could be changed to a number (0:pending, 1:completed) to save space
    """

    def __init__(self, room_id, date, start_time, end_time, status):
        self.room_id = room_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.status = status


# Create an engine and connect to the "bookings" database
engine = create_engine("sqlite:///bookings.db", echo=True)

# Create the "bookings" table in the database
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to create a new Booking instance and store it in the database
def store_booking_in_database(room_id, date, start_time, end_time, status="pending"):
    new_booking = Booking(room_id=room_id, date=date, start_time=start_time, end_time=end_time, status=status)
    session.add(new_booking)

    # Commit the transaction to save the booking to the database + Close the session
    session.commit()
    session.close()
