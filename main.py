from database import initialize_db, Session
from cli import add_hotel, add_room, book_room, view_room, view_bookings, delete_unoccupied_room, update_booking

def main_menu():
    """Main menu for the hotel management system."""
    with Session() as session:
        while True:
            print("\nMain Menu:")
            print("1. Add Hotel")
            print("2. Add Room")
            print("3. Book Room")
            print("4. View Rooms")
            print("5. View Bookings")
            print("6. Delete Unoccupied Room")
            print("7. Update Booking")  
            print("8. Exit")

            choice = input("Enter your choice: ").strip()
            if choice == "1":
                hotel_name = input("Hotel Name: ")
                checking_time = input("Check-in Time (HH:MM): ")
                checkout_time = input("Check-out Time (HH:MM): ")
                add_hotel(session, hotel_name, checking_time, checkout_time)
            elif choice == "2":
                hotel_id = int(input("Hotel ID: "))
                room_number = input("Room Number: ")
                room_type = input("Room Type (Single/Double/Suite): ")
                price = float(input("Price: "))
                add_room(session, hotel_id, room_number, room_type, price)
            elif choice == "3":
                room_id = int(input("Room ID: "))
                guest_name = input("Guest Name: ")
                contact_info = input("Contact Info: ")
                book_room(session, room_id, guest_name, contact_info)
            elif choice == "4":
                view_room(session)
            elif choice == "5":
                view_bookings(session)
            elif choice == "6":
                room_id = int(input("Room ID to delete: "))
                delete_unoccupied_room(session, room_id)
            elif choice == "7":
                booking_id = int(input("Booking ID to update: "))
                new_guest_name = input("New Guest Name (Leave blank to keep current): ").strip() or None
                new_contact_info = input("New Contact Info (Leave blank to keep current): ").strip() or None
                update_booking(session, booking_id, new_guest_name, new_contact_info)
            elif choice == "8":
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    initialize_db()
    main_menu()
