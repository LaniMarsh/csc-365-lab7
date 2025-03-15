from rooms import get_rooms_and_rates
from reservations import make_reservation, cancel_reservation, search_reservations
from revenue import get_revenue
from database import check_lab7_tables

def main():
    while True:
        print("\nHotel Management System")
        print("1. View Rooms")
        print("2. Make Reservation")
        print("3. Cancel Reservation")
        print("4. Search Reservations")
        print("5. View Revenue")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            get_rooms_and_rates()
        elif choice == "2":
            make_reservation()
        elif choice == "3":
            cancel_reservation()
        elif choice == "4":
            search_reservations()
        elif choice == "5":
            get_revenue()
        elif choice == "6":
            break

if __name__ == "__main__":
    check_lab7_tables()
    main()