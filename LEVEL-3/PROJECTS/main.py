# main.py
import student_ops as so

# Add Students
print(so.add_student(101, "Alice", "A"))
print(so.add_student(102, "Bob", "B"))
print(so.add_student(103, "Charlie", "C"))

# List Students
print("\n", so.list_students())

# Update Grade
print("\n", so.update_grade(102, "A+"))

# Find a Student
student = so.find_student(103)
print("\nDetails of roll number 103:")
print(student)
