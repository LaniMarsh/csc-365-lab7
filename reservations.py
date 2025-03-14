from database import connect_db

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

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    room_code = input("Room Code (or 'Any'): ")
    bed_type = input("Bed Type (or 'Any'): ")
    checkin = input("Check-in Date (YYYY-MM-DD): ")
    checkout = input("Check-out Date (YYYY-MM-DD): ")
    adults = int(input("Number of Adults: "))
    kids = int(input("Number of Kids: "))

    query = """
    SELECT RoomCode, RoomName, bedType, basePrice FROM lab7_rooms 
    WHERE (RoomCode = %s OR %s = 'Any') 
      AND (bedType = %s OR %s = 'Any')
      AND maxOcc >= %s
      AND RoomCode NOT IN (
          SELECT Room FROM lab7_reservations 
          WHERE CheckIn < %s AND Checkout > %s
      )
    LIMIT 5;
    """
    cursor.execute(query, (room_code, room_code, bed_type, bed_type, adults + kids, checkout, checkin))
    available_rooms = cursor.fetchall()

    if not available_rooms:
        print("No exact matches")

    # Suggest alternatives
    for i, room in enumerate(available_rooms, 1):
        print(f"{i}. {room['RoomName']} - {room['bedType']} - ${room['basePrice']} per night")

    choice = int(input("Enter the option number to book: "))
    selected_room = available_rooms[choice - 1]

    insert_query = """
    INSERT INTO lab7_reservations (CODE, Room, CheckIn, Checkout, Rate, LastName, FirstName, Adults, Kids)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    cursor.execute(insert_query, (None, selected_room['RoomCode'], checkin, checkout, selected_room['basePrice'], last_name, first_name, adults, kids))
    conn.commit()
    print(f"Reservation confirmed for {first_name} {last_name} in {selected_room['RoomName']}")

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