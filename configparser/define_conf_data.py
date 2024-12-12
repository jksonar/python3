import configparser

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'ServerAliveInterval': '45',
    'Compression': 'yes',
    'CompressionLevel': '9'
}

config['bitbucket.org'] = {
    'User': 'hg'
}

config['topsecret.server.com'] = {
    'Host Port': '50022',
    'ForwardX11': 'no'
}

with open('example.ini', 'w') as configfile:
    config.write(configfile)

# Generated example.ini:
# [DEFAULT]
# ServerAliveInterval = 45
# Compression = yes
# CompressionLevel = 9

# [bitbucket.org]
# User = hg

# [topsecret.server.com]
# Host Port = 50022
# ForwardX11 = no
