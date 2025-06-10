import csv
from collections import defaultdict
from datetime import datetime

def summarize_expenses(csv_path):
    monthly_summary = defaultdict(float)
    category_summary = defaultdict(float)

    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date, category, amount, _ = row
            try:
                amount = float(amount)
                month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
                monthly_summary[month] += amount
                category_summary[category] += amount
            except:
                continue

    print("\n--- Monthly Summary ---")
    for month, total in sorted(monthly_summary.items()):
        print(f"{month}: ₹{total:.2f}")

    print("\n--- Category Summary ---")
    for category, total in sorted(category_summary.items()):
        print(f"{category}: ₹{total:.2f}")

    input("\nPress Enter to continue...")