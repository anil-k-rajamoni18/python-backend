import csv

def view_expenses(csv_path):
    print("\n--- All Expenses ---")
    with open(csv_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            print(f"{row[0]} | {row[1]} | ₹{row[2]} | {row[3]}")
    input("\nPress Enter to continue...")