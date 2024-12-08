# Sync Over SSH
from sh import rsync

source = "/path/to/source/"
destination = "user@remote_host:/path/to/destination/"

rsync("-avz", "-e", "ssh", source, destination)
print("Remote sync completed.")
