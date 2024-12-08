# Dry Run to Preview Changes
from sh import rsync

source = "/path/to/source/"
destination = "/path/to/destination/"

rsync("-avz", "--dry-run", source, destination)
print("Dry run completed.")
