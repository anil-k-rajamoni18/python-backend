from student_management.base import Student

class Postgraduate(Student):
    def __init__(self, student_id: int, name: str, age: int, thesis_title: str):
        super().__init__(student_id, name, age)
        self.thesis_title = thesis_title

    def save_to_db(self):
        existing = self.db.fetchone("SELECT id FROM students WHERE id=?", (self.student_id,))
        if existing:
            self.db.execute(
                "UPDATE students SET name=?, age=?, type=?, thesis=?, year=NULL WHERE id=?",
                (self.name, self.age, 'postgrad', self.thesis_title, self.student_id)
            )
        else:
            self.db.execute(
                "INSERT INTO students (id, name, age, type, thesis) VALUES (?, ?, ?, ?, ?)",
                (self.student_id, self.name, self.age, 'postgrad', self.thesis_title)
            )

    def __str__(self):
        return f"Postgraduate {super().__str__()} (Thesis: {self.thesis_title})"
