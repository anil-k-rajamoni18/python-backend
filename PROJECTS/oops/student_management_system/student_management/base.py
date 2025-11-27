from student_management.db import Database

class Student:
    db = Database()

    def __init__(self, student_id: int, name: str, age: int):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.courses = {}

    def save_to_db(self):
        # Insert or update student record
        existing = self.db.fetchone("SELECT id FROM students WHERE id=?", (self.student_id,))
        if existing:
            self.db.execute(
                "UPDATE students SET name=?, age=? WHERE id=?",
                (self.name, self.age, self.student_id)
            )
        else:
            # For base class, type and extra fields unknown
            self.db.execute(
                "INSERT INTO students (id, name, age, type) VALUES (?, ?, ?, ?)",
                (self.student_id, self.name, self.age, 'base')
            )

    def add_course(self, course_name: str, grade: str):
        self.db.execute(
            "INSERT INTO courses (student_id, course_name, grade) VALUES (?, ?, ?)",
            (self.student_id, course_name, grade)
        )

    def get_courses(self):
        rows = self.db.fetchall(
            "SELECT course_name, grade FROM courses WHERE student_id=?",
            (self.student_id,)
        )
        return {course: grade for course, grade in rows}

    def get_transcript(self):
        courses = self.get_courses()
        transcript = f"Transcript for {self.name}:\n"
        transcript += "\n".join(f"{c}: {g}" for c, g in courses.items())
        return transcript

    def __str__(self):
        return f"{self.student_id} - {self.name}, Age: {self.age}"
