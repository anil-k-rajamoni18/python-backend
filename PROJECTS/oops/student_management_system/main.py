from student_management.manager import StudentManager
from student_management.undergrad import Undergraduate
from student_management.postgrad import Postgraduate

def main():
    manager = StudentManager()

    # Add students
    u1 = Undergraduate(1, "Alice Smith", 20, 2)
    u1.save_to_db()
    u1.add_course("Math", "A")
    u1.add_course("History", "B+")
    
    p1 = Postgraduate(2, "Bob Johnson", 27, "AI in Healthcare")
    p1.save_to_db()
    p1.add_course("Research Methodology", "A")
    
    # List all students
    print("\nAll Students:")
    for student in manager.list_students():
        print(student)
        print(student.get_transcript())
        print("----")

    # Search students by name
    print("\nSearch 'Alice':")
    for s in manager.search_students_by_name("Alice"):
        print(s)

    # Delete student
    print("\nDeleting student with ID 1...")
    manager.delete_student(1)

    print("\nAll Students after deletion:")
    for student in manager.list_students():
        print(student)

if __name__ == "__main__":
    main()
