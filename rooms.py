from database import connect_db


def get_rooms_and_rates():
    conn = connect_db()
    if not conn:
        return

    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT r.*, 
           COUNT(res.CODE) / 180 AS popularity_score, 
           (SELECT MIN(CheckIn) FROM lab7_reservations WHERE Room = r.RoomCode AND CheckIn > CURDATE()) AS next_checkin,
           DATEDIFF(Checkout, CheckIn) AS last_stay_duration,
           Checkout AS last_checkout
    FROM lab7_rooms r
    LEFT JOIN lab7_reservations res ON r.RoomCode = res.Room
    WHERE CheckIn >= DATE_SUB(CURDATE(), INTERVAL 180 DAY)
    GROUP BY r.RoomCode
    ORDER BY popularity_score DESC;
    """

    cursor.execute(query)
    rooms = cursor.fetchall()
    conn.close()

    for room in rooms:
        print(
            f"Room: {room['RoomName']} "
            f"| Beds: {room['Beds']} "
            f"| Popularity: {room['popularity_score']:.2f} "
            f"| Next Check-in: {room['next_checkin']}")
