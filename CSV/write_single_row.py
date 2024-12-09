import csv

with open("output.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(["Name", "Age", "City"])
