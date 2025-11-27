import pytest
import os
from todo.db import Database

TEST_DB = "test_tasks.db"

@pytest.fixture(scope="function")
def db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    db = Database(TEST_DB)
    yield db
    db.close()
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
