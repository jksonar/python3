import configparser

config = configparser.ConfigParser()

# a. Handle Missing Sections
try:
    value = config['nonexistent_section']['key']
except KeyError:
    print("Section not found")

# b. Handle Missing Options
try:
    value = config['database']['nonexistent_key']
except KeyError:
    print("Key not found")
