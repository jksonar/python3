import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Skip header row
    print(f"Headers: {headers}")
    for row in csv_reader:
        print(row)
# If the CSV file has a header row, skip it: