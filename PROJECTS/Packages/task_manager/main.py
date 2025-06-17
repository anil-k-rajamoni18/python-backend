from core.manager import handle_menu
import os

def ensure_project_dir():
    if not os.path.exists("projects"):
        os.makedirs("projects")

def main():
    ensure_project_dir()
    while True:
        print("\n=== Project Task Manager ===")
        print("1. Manage a project")
        print("2. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            project = input("Enter project name: ").strip()
            handle_menu(project)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
    