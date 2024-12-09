# Convert CSV to JSON
import csv
import json

with open("example.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

with open("output.json", mode="w") as json_file:
    json.dump(data, json_file, indent=4)
