# Using Interpolation

# Interpolation allows you to reference other values within the configuration file.
# a. Basic Interpolation
# [DEFAULT]
# base_dir = /home/user

# [paths]
# logs = %(base_dir)s/logs

import configparser

config = configparser.ConfigParser()

print(config['paths']['logs'])  # Output: /home/user/logs

# b. Disable Interpolation
config = configparser.ConfigParser(interpolation=None)
