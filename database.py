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
            print("No lab7 tables found. You may need to create them.")
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

        print("Tables created")
        conn.commit()
        conn.close()

if __name__ == "__main__":
    check_lab7_tables()

