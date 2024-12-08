from sh import rsync

source = "/path/to/source/"
destination = "/path/to/destination/"

rsync("-avz", source, destination)
print("Sync completed successfully!")
