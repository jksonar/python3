# Exclude Files
from sh import rsync

source = "/path/to/source/"
destination = "/path/to/destination/"
exclude_pattern = "*.log"

rsync("-avz", "--exclude", exclude_pattern, source, destination)
print("Sync completed with exclusion.")
