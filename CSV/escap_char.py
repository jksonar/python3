# Quoting and Escaping Special Characters
import csv

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ['Charlie, "The Great"', 35, "Chicago"]
]

with open("quoted_output.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file, quoting=csv.QUOTE_ALL)  # Quote all fields
    csv_writer.writerows(data)
