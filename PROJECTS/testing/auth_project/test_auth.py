import pytest
from auth import SQLiteAuthService

@pytest.fixture
def auth_service():
    # Use in-memory DB so no files are created
    return SQLiteAuthService(":memory:")

def test_register_and_login(auth_service):
    assert auth_service.register("alice", "password123") is True
    assert auth_service.login("alice", "password123") is True

def test_duplicate_user(auth_service):
    auth_service.register("bob", "secure123")
    with pytest.raises(ValueError, match="Username already exists"):
        auth_service.register("bob", "anotherpass")

def test_short_password(auth_service):
    with pytest.raises(ValueError, match="Password too short"):
        auth_service.register("tiny", "123")

def test_login_invalid(auth_service):
    auth_service.register("charlie", "abc123")
    assert auth_service.login("charlie", "wrongpass") is False

def test_is_registered(auth_service):
    auth_service.register("dave", "pass123")
    assert auth_service.is_registered("dave")
    assert not auth_service.is_registered("ghost")
