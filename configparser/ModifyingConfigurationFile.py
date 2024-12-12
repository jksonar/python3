import configparser
# a. Add a New Section
config = configparser.ConfigParser()
config['new_section'] = {
    'Setting1': 'Value1',
    'Setting2': 'Value2'
}

with open('example.ini', 'w') as configfile:
    config.write(configfile)

# b. Update Existing Key
config['DEFAULT']['Compression'] = 'no'

with open('example.ini', 'w') as configfile:
    config.write(configfile)

# c. Remove Section or Option
config.remove_section('new_section')
config.remove_option('DEFAULT', 'Compression')

with open('example.ini', 'w') as configfile:
    config.write(configfile)
