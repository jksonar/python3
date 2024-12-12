# Reading a Configuration File
# a. Load and Access Sections
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

# List all sections
print(config.sections())  # Output: ['bitbucket.org', 'topsecret.server.com']

# Access specific section
print(config['bitbucket.org']['User'])  # Output: hg

# Access default values
print(config['bitbucket.org']['Compression'])  # Output: yes

# b. Check for Section/Key Existence
if 'topsecret.server.com' in config:
    print("Section exists")

if config.has_option('DEFAULT', 'Compression'):
    print("Key exists in DEFAULT section")
