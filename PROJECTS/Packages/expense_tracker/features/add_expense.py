import csv
from utils.helpers import is_valid_date, get_today

def add_expense(csv_path):
    date = input("Date (YYYY-MM-DD) [leave blank for today]: ").strip()
    if not date:
        date = get_today()
    elif not is_valid_date(date):
        print("❌ Invalid date format.")
        return

    category = input("Category: ").strip()
    amount = input("Amount: ").strip()
    try:
        float(amount)
    except ValueError:
        print("❌ Amount must be a number.")
        return
    description = input("Description: ").strip()

    with open(csv_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully.")