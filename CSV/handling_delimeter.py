# Handling Different Delimiters
import csv

with open("example.csv", mode="r") as file:
    csv_reader = csv.reader(file, delimiter=";")  # Using semicolon as delimiter
    for row in csv_reader:
        print(row)
