# student_ops.py

students = []

def add_student(roll_no, name, grade):
    student = {
        "roll_no": roll_no,
        "name": name,
        "grade": grade
    }
    students.append(student)
    return f"Student {name} added."

def list_students():
    if not students:
        return "No students found."
    result = "Student List:\n"
    for s in students:
        result += f"{s['roll_no']} - {s['name']} - Grade: {s['grade']}\n"
    return result

def update_grade(roll_no, new_grade):
    for student in students:
        if student['roll_no'] == roll_no:
            student['grade'] = new_grade
            return f"Updated grade for {student['name']}."
    return "Student not found."

def find_student(roll_no):
    for student in students:
        if student['roll_no'] == roll_no:
            return student
    return "Student not found."
