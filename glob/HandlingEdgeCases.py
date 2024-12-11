import glob

# No Matches
# If no files match the pattern, glob returns an empty list:

files = glob.glob("*.nonexistent")
print(files)  # Output: []

# Case Sensitivity
# On Windows, patterns are case-insensitive; on Linux/macOS, they are case-sensitive.