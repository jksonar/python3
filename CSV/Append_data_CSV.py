import csv

new_data = [["Charlie", 35, "Chicago"]]

with open("output.csv", mode="a", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(new_data)
