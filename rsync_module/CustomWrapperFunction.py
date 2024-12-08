# Custom Wrapper Function
from sh import rsync

def sync_files(source, destination, options=None):
    if options is None:
        options = []
    rsync(*options, source, destination)

# Example usage
sync_files("/path/to/source/", "/path/to/destination/", options=["-avz", "--delete"])
