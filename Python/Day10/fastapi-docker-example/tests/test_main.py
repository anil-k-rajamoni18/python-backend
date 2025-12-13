# tests/test_main.py

import pytest
from fastapi.testclient import TestClient

import app.main as main  # so we can reset `users` reliably

client = TestClient(main.app)


@pytest.fixture(autouse=True)
def clear_users():
    """
    Automatically run before each test to reset the in-memory users list.
    """
    main.users = []
    yield
    main.users = []


def test_home_route():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI running inside Docker 🚀!"}


def test_create_user():
    new_user = {"id": 1, "name": "Alice"}
    response = client.post("/user/", json=new_user)

    assert response.status_code == 200
    assert response.json() == new_user
    # Ensure user stored in global list
    assert main.users == [new_user]


def test_list_users_after_creation():
    user1 = {"id": 1, "name": "Alice"}
    user2 = {"id": 2, "name": "Bob"}

    client.post("/user/", json=user1)
    client.post("/user/", json=user2)

    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == [user1, user2]


def test_get_existing_user():
    user = {"id": 1, "name": "Alice"}
    client.post("/user/", json=user)

    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == user


def test_get_non_existing_user():
    response = client.get("/user/999")
    assert response.status_code == 200  # Your code returns 200 with error payload
    assert response.json() == {"error": "User not found"}


def test_delete_existing_user():
    user = {"id": 1, "name": "Alice"}
    client.post("/user/", json=user)

    delete_response = client.delete("/user/1")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "User deleted"}

    # Ensure user is removed
    list_response = client.get("/users/")
    assert list_response.status_code == 200
    assert list_response.json() == []


def test_delete_non_existing_user():
    # Deleting a non-existing user still returns "User deleted" in current logic
    response = client.delete("/user/999")
    assert response.status_code == 200
    assert response.json() == {"message": "User deleted"}

    # Still no users
    list_response = client.get("/users/")
    assert list_response.json() == []


def test_update_existing_user():
    original_user = {"id": 1, "name": "Alice"}
    updated_user = {"id": 1, "name": "Alice Updated"}

    client.post("/user/", json=original_user)

    response = client.put("/user/1", json=updated_user)
    assert response.status_code == 200
    assert response.json() == updated_user

    # Confirm list reflects the update
    list_response = client.get("/users/")
    assert list_response.json() == [updated_user]


def test_update_non_existing_user():
    updated_user = {"id": 999, "name": "Ghost"}

    response = client.put("/user/999", json=updated_user)
    assert response.status_code == 200  # still 200 with error payload
    assert response.json() == {"error": "User not found"}
