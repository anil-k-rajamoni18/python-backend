import pytest
import os
from student_management.db import Database

TEST_DB = "test_students.db"

@pytest.fixture(scope="function")
def db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    db = Database(TEST_DB)
    yield db
    # Teardown
    db.close()
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
