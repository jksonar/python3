import csv

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"}
]

with open("output.csv", mode="w", newline="") as file:
    fieldnames = ["Name", "Age", "City"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    csv_writer.writeheader()  # Write the header row
    csv_writer.writerows(data)  # Write multiple rows
