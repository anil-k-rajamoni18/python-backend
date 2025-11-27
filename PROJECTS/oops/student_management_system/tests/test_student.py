import pytest
from student_management.base import Student
from student_management.undergrad import Undergraduate
from student_management.postgrad import Postgraduate

def test_create_student(db):
    s = Student(1, "John Doe", 21)
    s.save_to_db()
    loaded = Student.db.fetchone("SELECT * FROM students WHERE id=1")
    assert loaded[1] == "John Doe"
    assert loaded[2] == 21

def test_undergrad_save_and_load(db):
    u = Undergraduate(2, "Alice", 19, 3)
    u.save_to_db()
    loaded = Undergraduate.db.fetchone("SELECT * FROM students WHERE id=2")
    assert loaded[1] == "Alice"
    assert loaded[4] == 3  # year field

def test_postgrad_save_and_load(db):
    p = Postgraduate(3, "Bob", 26, "Quantum Computing")
    p.save_to_db()
    loaded = Postgraduate.db.fetchone("SELECT * FROM students WHERE id=3")
    assert loaded[1] == "Bob"
    assert loaded[5] == "Quantum Computing"  # thesis field

def test_add_course_and_transcript(db):
    s = Student(4, "Charlie", 22)
    s.save_to_db()
    s.add_course("Physics", "A")
    s.add_course("Chemistry", "B+")
    courses = s.get_courses()
    assert courses["Physics"] == "A"
    assert courses["Chemistry"] == "B+"
    transcript = s.get_transcript()
    assert "Physics: A" in transcript
    assert "Chemistry: B+" in transcript
