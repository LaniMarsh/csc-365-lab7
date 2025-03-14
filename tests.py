import unittest
from unittest.mock import patch, MagicMock
from rooms import get_rooms_and_rates
from reservations import make_reservation, cancel_reservation, search_reservations
from revenue import get_revenue

class TestRooms(unittest.TestCase):

    @patch("rooms.connect_db")
    def test_get_rooms_and_rates(self, mock_connect_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            {'RoomName': 'Suite', 'Beds': 2, 'popularity_score': 0.75, 'next_checkin': '2025-04-01'}
        ]

        get_rooms_and_rates()

        mock_cursor.execute.assert_called_once()
        self.assertTrue(mock_cursor.fetchall.called)

    @patch("reservations.connect_db")
    @patch("builtins.input", side_effect=["John", "Doe", "A101", "King", "2025-04-01", "2025-04-05", "2", "1", "1"])
    def test_make_reservation(self, mock_input, mock_connect_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            {'RoomCode': 'A101', 'RoomName': 'Suite', 'basePrice': 100.0}
        ]

        make_reservation()

        mock_cursor.execute.assert_called()
        self.assertTrue(mock_conn.commit.called)

    @patch("reservations.connect_db")
    @patch("builtins.input", side_effect=["12345", "yes"])
    def test_cancel_reservation(self, mock_input, mock_connect_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchone.return_value = {'CODE': 12345}

        cancel_reservation()

        mock_cursor.execute.assert_called_with("DELETE FROM lab7_reservations WHERE CODE = %s", ("12345",))
        self.assertTrue(mock_conn.commit.called)

    @patch("reservations.connect_db")
    @patch("builtins.input", side_effect=["John", "Doe", "A101"])
    def test_search_reservations(self, mock_input, mock_connect_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            {'CODE': 12345, 'FirstName': 'John', 'LastName': 'Doe', 'Room': 'A101'}
        ]

        search_reservations()

        mock_cursor.execute.assert_called()
        self.assertTrue(mock_cursor.fetchall.called)

    @patch("revenue.connect_db")
    def test_get_revenue(self, mock_connect_db):
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_connect_db.return_value = mock_conn
        mock_conn.cursor.return_value = mock_cursor

        mock_cursor.fetchall.return_value = [
            {'Room': 'A101', 'Jan': 500, 'Feb': 300, 'Mar': 400, 'Total': 1200}
        ]

        get_revenue()

        mock_cursor.execute.assert_called()
        self.assertTrue(mock_cursor.fetchall.called)


if __name__ == "__main__":
    unittest.main()
