import configparser

config = configparser.ConfigParser()

# a. Iterate Over Sections
for section in config.sections():
    print(f"Section: {section}")
    for key, value in config[section].items():
        print(f"  {key} = {value}")

# b. Iterate Over Keys in a Section
for key in config['bitbucket.org']:
    print(f"{key} = {config['bitbucket.org'][key]}")
