from models import Hotel, Room, Booking
from sqlalchemy.orm import sessionmaker

def add_hotel(session, hotel_name, checking_time, checkout_time):
    hotel = Hotel(name=hotel_name, check_in_time=checking_time, check_out_time=checkout_time)
    session.add(hotel)
    session.commit()
    print(f"Hotel '{hotel_name}' added.")

def add_room(session, hotel_id, room_number, room_type, price):
    room = Room(hotel_id=hotel_id, room_number=room_number, room_type=room_type, price=price)
    session.add(room)
    session.commit()
    print(f"Room {room_number} added to hotel ID {hotel_id}.")

def book_room(session, room_id, guest_name, contact_info):
    room = session.query(Room).filter(Room.room_id == room_id).first()
    if room:
        booking = Booking(room_id=room_id, guest_name=guest_name, contact_info=contact_info)
        session.add(booking)
        session.commit()
        print(f"Room {room.room_number} booked for {guest_name}.")
    else:
        print(f"Room ID {room_id} not found.")

def view_room(session):
    rooms = session.query(Room).all()
    for room in rooms:
        print(f"Room {room.room_number} ({room.room_type}) - ${room.price}")

def view_bookings(session):
    bookings = session.query(Booking).all()
    for booking in bookings:
        print(f"Booking ID: {booking.booking_id}, Guest: {booking.guest_name}, Room: {booking.room.room_number}")

def delete_unoccupied_room(session, room_id):
    room = session.query(Room).filter(Room.room_id == room_id).first()
    if room:
        if not session.query(Booking).filter(Booking.room_id == room_id).first():
            session.delete(room)
            session.commit()
            print(f"Room {room.room_number} deleted.")
        else:
            print(f"Room {room.room_number} is occupied and cannot be deleted.")
    else:
        print(f"Room ID {room_id} not found.")

def update_booking(session, booking_id, new_guest_name=None, new_contact_info=None):
    booking = session.query(Booking).filter(Booking.booking_id == booking_id).first()
    if booking:
        if new_guest_name:
            booking.guest_name = new_guest_name
        if new_contact_info:
            booking.contact_info = new_contact_info
        session.commit()
        print(f"Booking {booking_id} updated.")
    else:
        print(f"Booking ID {booking_id} not found.")
