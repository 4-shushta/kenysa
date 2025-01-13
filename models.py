from datetime import datetime
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, ForeignKey, DateTime, CheckConstraint
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'
    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_name = Column(String, nullable=False)
    check_in_time = Column(String, nullable=False)  # Check-in time for the hotel
    check_out_time = Column(String, nullable=False)  # Check-out time for the hotel

    rooms = relationship("Room", back_populates="hotel", cascade="all, delete-orphan")

class Room(Base):
    __tablename__ = 'rooms'
    room_id = Column(Integer, primary_key=True, autoincrement=True)
    hotel_id = Column(Integer, ForeignKey('hotels.hotel_id'), nullable=False)
    room_number = Column(String, nullable=False)  # Unique room number within a hotel
    room_type = Column(String, CheckConstraint("room_type IN ('Single', 'Double', 'Suite')"), nullable=False)
    status = Column(String, CheckConstraint("status IN ('available', 'booked')"), nullable=False, default="available")
    price = Column(Float, nullable=False)  # Price of the room per night

    hotel = relationship("Hotel", back_populates="rooms")
    bookings = relationship("Booking", back_populates="room", cascade="all, delete-orphan")

class Booking(Base):
    __tablename__ = 'bookings'
    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    guest_name = Column(String, nullable=False)
    contact_info = Column(String, nullable=False)
    hotel_id = Column(Integer, ForeignKey('hotels.hotel_id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.room_id'), nullable=False)
    booking_time = Column(DateTime, default=datetime.utcnow)  # Time when the booking was made

    room = relationship("Room", back_populates="bookings")
