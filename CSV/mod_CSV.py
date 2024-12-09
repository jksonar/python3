# Modifying a CSV File
import csv

# Read the file and modify data
modified_data = []
with open("example.csv", mode="r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        row[1] = int(row[1]) + 1  # Increment age by 1
        modified_data.append(row)

# Write the modified data back to the file
with open("example.csv", mode="w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(modified_data)
