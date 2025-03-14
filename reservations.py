from database import connect_db
from datetime import datetime

def cancel_reservation():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor()
    code = input("Enter reservation code to cancel: ")

    cursor.execute("SELECT * FROM lab7_reservations WHERE CODE = %s", (code,))
    reservation = cursor.fetchone()

    if not reservation:
        print("Reservation not found")
        return

    confirm = input(f"Are you sure you want to cancel reservation {code}? (yes/no): ")
    if confirm.lower() == "yes":
        cursor.execute("DELETE FROM lab7_reservations WHERE CODE = %s", (code,))
        conn.commit()
        print("Reservation canceled")


def make_reservation():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor(dictionary=True)

    try:
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        room_code = input("Room Code (or 'Any'): ").strip()
        bed_type = input("Bed Type (or 'Any'): ").strip()
        checkin = input("Check-in Date (YYYY-MM-DD): ").strip()
        checkout = input("Check-out Date (YYYY-MM-DD): ").strip()
        adults = int(input("Number of Adults: ").strip())
        kids = int(input("Number of Kids: ").strip())

        total_guests = adults + kids

        query = """
        SELECT RoomCode, RoomName, bedType, basePrice, maxOcc FROM lab7_rooms 
        WHERE (RoomCode = %s OR %s = 'Any') 
          AND (bedType = %s OR %s = 'Any')
          AND maxOcc >= %s
          AND RoomCode NOT IN (
              SELECT Room FROM lab7_reservations 
              WHERE CheckIn <= %s AND Checkout >= %s
          )
        LIMIT 5;
        """
        cursor.execute(query, (room_code, room_code, bed_type, bed_type, total_guests, checkout, checkin))
        available_rooms = cursor.fetchall()

        if not available_rooms:
            print("No exact matches found. Try adjusting your criteria.")
            return

        print("\nAvailable Rooms:")
        for i, room in enumerate(available_rooms, 1):
            print(f"{i}. {room['RoomName']} - {room['bedType']} - ${room['basePrice']} per night")

        while True:
            try:
                choice = int(input("\nEnter the option number to book (or 0 to cancel): ").strip())
                if choice == 0:
                    print("Reservation cancelled.")
                    return
                if 1 <= choice <= len(available_rooms):
                    selected_room = available_rooms[choice - 1]
                    break
                else:
                    print("Invalid option. Please select a valid room number.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        cursor.execute("SELECT MAX(CODE) + 1 AS new_code FROM lab7_reservations;")
        new_code = cursor.fetchone()["new_code"] or 1  # Default to 1 if no reservations exist

        insert_query = """
        INSERT INTO lab7_reservations (CODE, Room, CheckIn, Checkout, Rate, LastName, FirstName, Adults, Kids)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cursor.execute(insert_query, (new_code, selected_room['RoomCode'], checkin, checkout, selected_room['basePrice'], last_name, first_name, adults, kids))
        conn.commit()

        checkin_int = datetime.strptime(checkin, "%Y-%m-%d")
        checkout_int = datetime.strptime(checkout, "%Y-%m-%d")

        total_nights = (checkout_int - checkin_int).days

        print(f"\n Reservation confirmed for {first_name} {last_name} in {selected_room['RoomName']} ({selected_room['bedType']}).")
        print(f"Check-in: {checkin}, Check-out: {checkout}")
        print(f"Guests: {adults} Adults, {kids} Kids")
        print(f"Total cost: ${selected_room['basePrice'] * total_nights} (excluding weekend surcharge)")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def search_reservations():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor(dictionary=True)

    first_name = input("First Name (or leave blank): ").strip()
    last_name = input("Last Name (or leave blank): ").strip()
    room_code = input("Room Code (or leave blank): ").strip()

    query = """
    SELECT * FROM lab7_reservations 
    WHERE (FirstName LIKE %s OR %s = '') 
      AND (LastName LIKE %s OR %s = '') 
      AND (Room LIKE %s OR %s = '');
    """
    cursor.execute(query, (f"%{first_name}%", first_name, f"%{last_name}%", last_name, f"%{room_code}%", room_code))
    results = cursor.fetchall()

    if not results:
        print("No reservations found.")
    else:
        for res in results:
            print(f"{res['CODE']} - {res['FirstName']} {res['LastName']} | Room: {res['Room']} | Check-in: {res['CheckIn']} | Check-out: {res['Checkout']} | Rate: ${res['Rate']}")

    cursor.close()
    conn.close()