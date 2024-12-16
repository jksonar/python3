import os
import configparser
    

def get_config(config_file, section_name=None):
    """
    load configuration file (like .ini).
    See "https://docs.python.org/2/library/configparser.html" for detail.
    """
    if not os.path.isfile(config_file):
        raise ValueError('Config file "{}" not exists'.format(config_file))
    conf = configparser.ConfigParser()
    conf.read(config_file)
    if not section_name:
        return conf
    section = conf.items(section_name)
    section = dict(section)
    return section
