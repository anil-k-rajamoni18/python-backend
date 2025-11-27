from typing import List, Optional
from student_management.base import Student
from student_management.undergrad import Undergraduate
from student_management.postgrad import Postgraduate
from student_management.db import Database

class StudentManager:
    def __init__(self):
        self.db = Database()

    def add_student(self, student: Student):
        student.save_to_db()

    def get_student(self, student_id: int) -> Optional[Student]:
        row = self.db.fetchone("SELECT * FROM students WHERE id=?", (student_id,))
        if not row:
            return None
        id_, name, age, type_, year, thesis = row
        if type_ == 'undergrad':
            student = Undergraduate(id_, name, age, year)
        elif type_ == 'postgrad':
            student = Postgraduate(id_, name, age, thesis)
        else:
            student = Student(id_, name, age)
        # Load courses
        courses = self.db.fetchall("SELECT course_name, grade FROM courses WHERE student_id=?", (student_id,))
        for course_name, grade in courses:
            student.courses[course_name] = grade
        return student

    def delete_student(self, student_id: int):
        self.db.execute("DELETE FROM courses WHERE student_id=?", (student_id,))
        self.db.execute("DELETE FROM students WHERE id=?", (student_id,))

    def list_students(self) -> List[Student]:
        rows = self.db.fetchall("SELECT id FROM students")
        return [self.get_student(row[0]) for row in rows]

    def search_students_by_name(self, name: str) -> List[Student]:
        pattern = f"%{name}%"
        rows = self.db.fetchall("SELECT id FROM students WHERE name LIKE ?", (pattern,))
        return [self.get_student(row[0]) for row in rows]
