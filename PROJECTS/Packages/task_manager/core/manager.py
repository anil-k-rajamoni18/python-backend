from data.file_ops import read_tasks, write_tasks
from utils.date_tools import today
from core.validator import is_valid_date

def handle_menu(project):
    file_path = f"projects/{project}.json"
    while True:
        print(f"\n--- Managing Project: {project} ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Task Title: ").strip()
            due = input("Due Date (YYYY-MM-DD): ").strip()
            if not is_valid_date(due):
                print("❌ Invalid date.")
                continue
            add_task(file_path, title, due)
        elif choice == '2':
            view_tasks(file_path)
        elif choice == '3':
            mark_done(file_path)
        elif choice == '4':
            delete_task(file_path)
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice.")

def add_task(path, title, due_date):
    tasks = read_tasks(path)
    tasks.append({
        "title": title,
        "due_date": due_date,
        "created_at": today(),
        "done": False
    })
    write_tasks(path, tasks)
    print("✅ Task added.")

def view_tasks(path):
    tasks = read_tasks(path)
    if not tasks:
        print("📭 No tasks found.")
        return
    print("\n📋 Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✅" if t['done'] else "❌"
        print(f"{i}. [{status}] {t['title']} (Due: {t['due_date']}, Created: {t['created_at']})")

def mark_done(path):
    tasks = read_tasks(path)
    view_tasks(path)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]['done'] = True
            write_tasks(path, tasks)
            print("✅ Task updated.")
        else:
            print("❌ Invalid number.")
    except:
        print("❌ Invalid input.")

def delete_task(path):
    tasks = read_tasks(path)
    view_tasks(path)
    if not tasks:
        return
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            del tasks[idx]
            write_tasks(path, tasks)
            print("🗑️ Task deleted.")
        else:
            print("❌ Invalid number.")
    except:
        print("❌ Invalid input.")