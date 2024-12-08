# Include and Exclude Files
from sh import rsync

source = "/path/to/source/"
destination = "/path/to/destination/"

rsync("-avz", "--include", "*.txt", "--exclude", "*", source, destination)
print("Included only .txt files.")
