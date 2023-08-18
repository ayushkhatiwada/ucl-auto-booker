from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine("sqlite:///bookings.db")
Base = declarative_base()

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    room_number = Column("room_number", String)
    room_id = Column("room_id", Integer)
    date = Column("date", String)
    start_time = Column("start_time", String)
    end_time = Column("end_time", String)
    request_made_time = Column("request_made_time", String)
    status = Column("status", String)
    booking_completed_time = Column("booking_completed_time", String)

Session = sessionmaker(bind=engine)
session = Session()

# Retrieve all bookings
bookings = session.query(Booking).all()

# Retrieve bookings for a specific room number (e.g., room_number=101)
room_bookings = session.query(Booking).filter_by(room_number="2.02").all()


