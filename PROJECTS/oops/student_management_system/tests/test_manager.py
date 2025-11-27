from student_management.manager import StudentManager
from student_management.undergrad import Undergraduate
from student_management.postgrad import Postgraduate

def test_add_and_get_student(db):
    manager = StudentManager()
    u = Undergraduate(10, "Diana", 20, 1)
    manager.add_student(u)
    fetched = manager.get_student(10)
    assert fetched.name == "Diana"
    assert fetched.year == 1

def test_list_students(db):
    manager = StudentManager()
    u = Undergraduate(11, "Eve", 21, 2)
    p = Postgraduate(12, "Frank", 25, "AI Ethics")
    manager.add_student(u)
    manager.add_student(p)
    students = manager.list_students()
    names = [s.name for s in students]
    assert "Eve" in names
    assert "Frank" in names

def test_delete_student(db):
    manager = StudentManager()
    u = Undergraduate(13, "Grace", 22, 3)
    manager.add_student(u)
    manager.delete_student(13)
    assert manager.get_student(13) is None

def test_search_students_by_name(db):
    manager = StudentManager()
    u = Undergraduate(14, "Hannah", 20, 1)
    p = Postgraduate(15, "Harry", 26, "Data Science")
    manager.add_student(u)
    manager.add_student(p)
    results = manager.search_students_by_name("Han")
    names = [s.name for s in results]
    assert "Hannah" in names
    assert "Harry" not in names
