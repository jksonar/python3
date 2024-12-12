import configparser

config = configparser.ConfigParser()

# a. Save Settings at Runtime
config['runtime'] = {
    'last_run': '2024-12-11',
    'status': 'success'
}

with open('runtime_config.ini', 'w') as configfile:
    config.write(configfile)

# b. Read Saved Settings
config.read('runtime_config.ini')
print(config['runtime']['last_run'])  # Output: 2024-12-11
