from utils.file_manager import initialize_file
from features.add_expense import add_expense
from features.view_expenses import view_expenses
from features.summary import summarize_expenses
from utils.helpers import clear_screen

CSV_PATH = "data/storage.csv"

def main():
    initialize_file(CSV_PATH)

    while True:
        clear_screen()
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(CSV_PATH)
        elif choice == '2':
            view_expenses(CSV_PATH)
        elif choice == '3':
            summarize_expenses(CSV_PATH)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
