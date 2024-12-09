import csv

with open("large_file.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Process each row
        print(row)
# Reading Large Files in Chunks