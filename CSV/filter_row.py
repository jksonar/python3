# Filtering Rows Based on a Condition
import csv

with open("example.csv", mode="r") as infile, open("filtered.csv", mode="w", newline="") as outfile:
    csv_reader = csv.reader(infile)
    csv_writer = csv.writer(outfile)
    
    for row in csv_reader:
        if int(row[1]) > 25:  # Filter rows where Age > 25
            csv_writer.writerow(row)
