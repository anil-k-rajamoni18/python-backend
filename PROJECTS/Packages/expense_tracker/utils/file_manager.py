import csv
import os

def initialize_file(path):
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(path):
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
