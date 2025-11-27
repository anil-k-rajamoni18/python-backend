from todo.task_manager import TaskManager
from todo.task import Task
import sys

def print_task(task: Task):
    print(task)
    print(f"  Description: {task.description}")
    if task.reminder:
        print(f"  Reminder: {task.reminder}")

def menu():
    print("\nTask Manager CLI")
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. List Tasks")
    print("5. Mark Task Complete")
    print("6. Exit")

def cli_loop():
    manager = TaskManager()
    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Title: ").strip()
            description = input("Description: ").strip()
            category = input("Category: ").strip()
            priority = int(input("Priority (0-10): ").strip())
            reminder = input("Reminder (YYYY-MM-DD HH:MM) [optional]: ").strip()
            reminder = reminder if reminder else None
            task = Task(title, description, category, priority, reminder)
            manager.add_task(task)
            print(f"Task added with ID {task.id}")

        elif choice == "2":
            task_id = int(input("Task ID to edit: "))
            task = manager.get_task(task_id)
            if not task:
                print("Task not found!")
                continue
            print("Leave blank to keep current value.")
            title = input(f"Title ({task.title}): ").strip() or task.title
            description = input(f"Description ({task.description}): ").strip() or task.description
            category = input(f"Category ({task.category}): ").strip() or task.category
            priority_input = input(f"Priority ({task.priority}): ").strip()
            priority = int(priority_input) if priority_input else task.priority
            reminder = input(f"Reminder ({task.reminder}): ").strip() or task.reminder
            completed_input = input(f"Completed (y/n) ({'y' if task.completed else 'n'}): ").strip().lower()
            completed = task.completed
            if completed_input == 'y':
                completed = True
            elif completed_input == 'n':
                completed = False
            task.title = title
            task.description = description
            task.category = category
            task.priority = priority
            task.reminder = reminder
            task.completed = completed
            manager.update_task(task)
            print("Task updated.")

        elif choice == "3":
            task_id = int(input("Task ID to delete: "))
            manager.delete_task(task_id)
            print("Task deleted.")

        elif choice == "4":
            filter_cat = input("Filter by category (leave blank for all): ").strip() or None
            filter_completed_input = input("Filter by status (pending/done/all): ").strip().lower()
            filter_completed = None
            if filter_completed_input == "pending":
                filter_completed = False
            elif filter_completed_input == "done":
                filter_completed = True
            tasks = manager.list_tasks(filter_cat, filter_completed)
            if not tasks:
                print("No tasks found.")
            for task in tasks:
                print_task(task)
                print("-" * 30)

        elif choice == "5":
            task_id = int(input("Task ID to mark complete: "))
            task = manager.get_task(task_id)
            if task:
                task.mark_complete()
                manager.update_task(task)
                print("Task marked as complete.")
            else:
                print("Task not found.")

        elif choice == "6":
            manager.close()
            print("Goodbye!")
            sys.exit()

        else:
            print("Invalid option, try again.")
