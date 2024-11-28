import os
path = "example.txt"
if os.path.isfile(path):
    print("It's a file.")
elif os.path.isdir(path):
    print("It's a directory.")
