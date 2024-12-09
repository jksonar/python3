import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)
# csv.DictReader reads each row as an OrderedDict where keys are column headers.