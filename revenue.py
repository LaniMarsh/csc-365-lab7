from database import connect_db

def get_revenue():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT Room, 
           SUM(CASE WHEN MONTH(CheckIn) = 1 THEN Rate ELSE 0 END) AS Jan,
           SUM(CASE WHEN MONTH(CheckIn) = 2 THEN Rate ELSE 0 END) AS Feb,
           SUM(CASE WHEN MONTH(CheckIn) = 3 THEN Rate ELSE 0 END) AS Mar,
           SUM(Rate) AS Total
    FROM lab7_reservations
    GROUP BY Room;
    """

    cursor.execute(query)
    rooms = cursor.fetchall()

    print("Revenue Report:")
    for room in rooms:
        print(f"Room {room['Room']}: ${room['Total']} Total")
