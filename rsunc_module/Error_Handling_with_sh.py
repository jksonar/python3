# Error Handling with sh
from sh import rsync, ErrorReturnCode

try:
    rsync("-avz", "/invalid/source/", "/path/to/destination/")
except ErrorReturnCode as e:
    print("Error occurred:")
    print(e.stderr.decode())  # Print error details
