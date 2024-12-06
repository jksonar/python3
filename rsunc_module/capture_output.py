from sh import rsync
# Capture Output

source = "/path/to/source/"
destination = "/path/to/destination/"

result = rsync("-avz", source, destination)
print(result)  # Captures and prints the output
