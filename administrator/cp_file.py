import os

source = "example.txt"
destination = "example_copy.txt"

with open(source, "rb") as src, open(destination, "wb") as dest:
    dest.write(src.read())

print("File copied successfully.")
