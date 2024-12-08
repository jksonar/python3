# Delete Extra Files at Destination
from sh import rsync

source = "/path/to/source/"
destination = "/path/to/destination/"

rsync("-avz", "--delete", source, destination)
print("Deleted files not in source.")
