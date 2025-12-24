import json
from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.fixture
def mock_db_connection():
    mock_conn = MagicMock()
    mock_cursor = MagicMock()

    mock_conn.__enter__ = MagicMock(return_value=mock_conn)
    mock_conn.__exit__ = MagicMock(return_value=False)

    mock_cursor.__enter__ = MagicMock(return_value=mock_cursor)
    mock_cursor.__exit__ = MagicMock(return_value=False)

    mock_conn.cursor.return_value = mock_cursor
    return mock_conn, mock_cursor


class TestHomeEndpoint:
    def test_home_returns_welcome_message(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {
            "message": "Hello, FastAPI running inside Docker 🚀!"
        }


class TestGetUser:
    @patch("app.main.get_connection")
    def test_get_user_success(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        user_data = {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
        }
        mock_cursor.fetchone.return_value = {
            "data": json.dumps(user_data)
        }

        response = client.get("/user/1")

        assert response.status_code == 200
        assert response.json() == user_data
        mock_cursor.execute.assert_called_once_with(
            "SELECT data FROM users WHERE id = %s",
            (1,),
        )

    @patch("app.main.get_connection")
    def test_get_user_not_found(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        mock_cursor.fetchone.return_value = None

        response = client.get("/user/999")

        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}



class TestCreateUser:
    @patch("app.main.get_connection")
    def test_create_user_success(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        new_user = {
            "id": 1,
            "name": "Jane Doe",
            "email": "jane@example.com",
        }

        response = client.post("/user/", json=new_user)

        assert response.status_code == 200
        assert response.json() == new_user
        mock_cursor.execute.assert_called_once_with(
            "INSERT INTO users (id, data) VALUES (%s, %s)",
            (1, json.dumps(new_user)),
        )
        mock_conn.commit.assert_called_once()

    @patch("app.main.get_connection")
    def test_create_user_without_id(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        response = client.post(
            "/user/",
            json={"name": "Jane Doe"},
        )

        assert response.status_code == 400
        assert response.json() == {
            "detail": "User must have an 'id' field"
        }

        mock_cursor.execute.assert_not_called()


class TestListUsers:
    @patch("app.main.get_connection")
    def test_list_users_success(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        users = [{"id": 1}, {"id": 2}]
        mock_cursor.fetchall.return_value = [
            {"data": json.dumps(user)} for user in users
        ]

        response = client.get("/users/")

        assert response.status_code == 200
        assert response.json() == users
        mock_cursor.execute.assert_called_once_with(
            "SELECT data FROM users"
        )

    @patch("app.main.get_connection")
    def test_list_users_empty(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        mock_cursor.fetchall.return_value = []

        response = client.get("/users/")

        assert response.status_code == 200
        assert response.json() == []


class TestDeleteUser:
    @patch("app.main.get_connection")
    def test_delete_user_success(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        mock_cursor.rowcount = 1

        response = client.delete("/user/1")

        assert response.status_code == 200
        assert response.json() == {"message": "User deleted"}
        mock_cursor.execute.assert_called_once_with(
            "DELETE FROM users WHERE id = %s",
            (1,),
        )
        mock_conn.commit.assert_called_once()

    @patch("app.main.get_connection")
    def test_delete_user_not_found(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        mock_cursor.rowcount = 0

        response = client.delete("/user/999")

        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}



class TestUpdateUser:
    @patch("app.main.get_connection")
    def test_update_user_success(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        mock_cursor.rowcount = 1
        updated_data = {"id": 1, "name": "Updated"}

        response = client.put("/user/1", json=updated_data)

        assert response.status_code == 200
        assert response.json() == updated_data
        mock_cursor.execute.assert_called_once_with(
            "UPDATE users SET data = %s WHERE id = %s",
            (json.dumps(updated_data), 1),
        )
        mock_conn.commit.assert_called_once()

    @patch("app.main.get_connection")
    def test_update_user_not_found(self, mock_get_conn, mock_db_connection):
        mock_conn, mock_cursor = mock_db_connection
        mock_get_conn.return_value = mock_conn

        mock_cursor.rowcount = 0

        response = client.put("/user/999", json={"id": 999})

        assert response.status_code == 404
        assert response.json() == {"detail": "User not found"}



class TestDatabaseInitialization:
    @patch("app.main.get_connection")
    def test_init_db_creates_table(self, mock_get_conn):
        from app.main import init_db

        mock_conn = MagicMock()
        mock_cursor = MagicMock()

        mock_conn.__enter__ = MagicMock(return_value=mock_conn)
        mock_conn.__exit__ = MagicMock(return_value=False)
        mock_cursor.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor.__exit__ = MagicMock(return_value=False)

        mock_conn.cursor.return_value = mock_cursor
        mock_get_conn.return_value = mock_conn

        init_db()

        mock_cursor.execute.assert_called_once()
        assert "CREATE TABLE IF NOT EXISTS users" in (
            mock_cursor.execute.call_args[0][0]
        )
        mock_conn.commit.assert_called_once()
