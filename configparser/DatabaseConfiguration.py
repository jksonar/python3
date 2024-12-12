# [database]
# host = localhost
# port = 5432
# user = admin
# password = secret
import configparser

config = configparser.ConfigParser()
config.read('db_config.ini')

db_config = config['database']
print(db_config['host'])  # Output: localhost

# Use Configuration in a Script
if config['DEFAULT'].getboolean('Compression'):
    print("Compression is enabled")

# Validate Configuration File
required_sections = ['database', 'logging']
for section in required_sections:
    if section not in config:
        raise ValueError(f"Missing section: {section}")
