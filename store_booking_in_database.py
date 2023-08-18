from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


# Define the base class for declarative models
Base = declarative_base()

# Define the Booking class
class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_number = Column("room_number", String)
    room_id = Column("room_id", Integer)
    date = Column("date", String)
    start_time = Column("start_time", String)
    end_time = Column("end_time", String)
    request_made_time = Column("request_made_time", String)
    """
    Status of booking. Options are:
    0. Requested - Booking has been saved to database
    1. Executing - Thread/Subprocess has been assigned to booking. Waiting for bookable window to open to execute booking 
    2. Complete - Booking completed
    Could be changed to a number (0:requested, 1:executing,  2:completed) to save space
    """
    status = Column("status", String)

    # Variable will not be initialised upon creation of booking request. Will be filled in after booking is completed 
    booking_completed_time = Column("booking_completed_time", String)


    def __init__(self, room_number, room_id, date, start_time, end_time, status, request_made_time):
        self.room_number = room_number
        self.room_id = room_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.request_made_time = request_made_time
        self.status = status


# Create an engine and connect to the "bookings" database
engine = create_engine("sqlite:///bookings.db", echo=True)

# Create the "bookings" table in the database
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to create a new Booking instance and store it in the database
def store_booking_in_database(room_number, room_id, date, start_time, end_time, request_made_time, status="requested"):
    new_booking = Booking(room_number=room_number, room_id=room_id, date=date, start_time=start_time, end_time=end_time, request_made_time=request_made_time, status=status)
    session.add(new_booking)

    # Commit the transaction to save the booking to the database + Close the session
    session.commit()
    session.close()
