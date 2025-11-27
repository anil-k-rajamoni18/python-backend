from student_management.base import Student

class Undergraduate(Student):
    def __init__(self, student_id: int, name: str, age: int, year: int):
        super().__init__(student_id, name, age)
        self.year = year

    def save_to_db(self):
        # Insert or update undergraduate student record
        existing = self.db.fetchone("SELECT id FROM students WHERE id=?", (self.student_id,))
        if existing:
            self.db.execute(
                "UPDATE students SET name=?, age=?, type=?, year=?, thesis=NULL WHERE id=?",
                (self.name, self.age, 'undergrad', self.year, self.student_id)
            )
        else:
            self.db.execute(
                "INSERT INTO students (id, name, age, type, year) VALUES (?, ?, ?, ?, ?)",
                (self.student_id, self.name, self.age, 'undergrad', self.year)
            )

    def __str__(self):
        return f"Undergraduate {super().__str__()} (Year {self.year})"