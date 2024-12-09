import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Opens a CSV file in read mode (r).
# csv.reader reads the file line by line and splits it into a list