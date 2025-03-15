import mysql.connector

def connect_db():
    print("Attempting to connect to the database...")
    try:
        conn = mysql.connector.connect(
            host="db.labthreesixfive.com",
            user="lmarsh12",
            password="Wtr25_365_028196733",
            database="lmarsh12"
        )
        if conn.is_connected():
            print("Successfully connected")
        return conn
    except mysql.connector.Error as e:
        print(f"Database connection failed: {e}")
        return None

def check_lab7_tables():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES LIKE 'lab7_%'")
        tables = cursor.fetchall()
        if tables:
            print("Found lab7 tables:")
            for table in tables:
                print(table[0])
        else:
            print("No lab7 tables found. Creating them now...")
            create_lab7_tables()
        conn.close()

def create_lab7_tables():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lab7_rooms (
          RoomCode CHAR(5) PRIMARY KEY,
          RoomName VARCHAR(30) NOT NULL UNIQUE,
          Beds INT NOT NULL,
          bedType VARCHAR(8) NOT NULL,
          maxOcc INT NOT NULL,
          basePrice DECIMAL(6,2) NOT NULL,
          decor VARCHAR(20) NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS lab7_reservations (
          CODE INT PRIMARY KEY,
          Room CHAR(5) NOT NULL,
          CheckIn DATE NOT NULL,
          Checkout DATE NOT NULL,
          Rate DECIMAL(6,2) NOT NULL,
          LastName VARCHAR(15) NOT NULL,
          FirstName VARCHAR(15) NOT NULL,
          Adults INT NOT NULL,
          Kids INT NOT NULL,
          FOREIGN KEY (Room) REFERENCES lab7_rooms(RoomCode)
        );
        """)

        print("Tables created successfully.")
        conn.commit()
        conn.close()

    # populate_lab7_tables()


def populate_lab7_tables():
    conn = connect_db()
    if conn:
        cursor = conn.cursor()

        print("Clearing existing data in lab7_rooms and lab7_reservations...")
        cursor.execute("DELETE FROM lab7_reservations;")
        cursor.execute("DELETE FROM lab7_rooms;")
        conn.commit()

        print("Populating lab7_rooms table...")
        cursor.executemany("""
            INSERT INTO lab7_rooms (RoomCode, RoomName, Beds, bedType, maxOcc, basePrice, decor)
            VALUES (%s, %s, %s, %s, %s, %s, %s);
        """, [
            ('A101', 'Deluxe Suite', 2, 'King', 4, 200.00, 'Modern'),
            ('B202', 'Economy Room', 1, 'Queen', 2, 100.00, 'Minimalist'),
            ('C303', 'Family Room', 3, 'Double', 6, 250.00, 'Rustic')
        ])
        print("lab7_rooms table populated.")

        print("Populating lab7_reservations table...")
        cursor.executemany("""
            INSERT INTO lab7_reservations (CODE, Room, CheckIn, Checkout, Rate, LastName, FirstName, Adults, Kids)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """, [
            (1001, 'A101', '2025-03-01', '2025-03-05', 200.00, 'Smith', 'John', 2, 0),
            (1002, 'B202', '2025-03-10', '2025-03-12', 100.00, 'Doe', 'Jane', 1, 1),
            (1003, 'C303', '2025-04-15', '2025-04-20', 250.00, 'Brown', 'Charlie', 4, 2)
        ])
        print("lab7_reservations table populated.")

        conn.commit()
        cursor.close()
        conn.close()
        print("Database setup complete.")


if __name__ == "__main__":
    populate_lab7_tables()
