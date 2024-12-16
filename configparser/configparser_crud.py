#  Examples of the Python core library module "ConfigParser", that helps you creating and interacting with configuration files. 
import os
import configparser

def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt")

    with open(path, "wb") as config_file:
        config.write(config_file)

def crudConfig(path):
    """
    Create, read, update, delete config
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    # Read some values from the config
    font = config.get("Settings", "font")
    font_size = config.get("Settings", "font_size")

    # Change a value in the config
    config.set("Settings", "font_size", "12")

    # Delete a value from the config
    config.remove_option("Settings", "font_style")

    # Write changes back to the config file
    with open(path, "wb") as config_file:
        config.write(config_file)

def interpolationDemo(path):
    """
    Interpolation: using options to build another option
    """
    if not os.path.exists(path):
        createConfig(path)

    config = configparser.ConfigParser()
    config.read(path)

    print(config.get("Settings", "font_info"))

    print(config.get("Settings", "font_info", 0,
        {"font": "Arial", "font_size": "100"}))

if __name__ == '__main__':
    path = "settings.ini"
    createConfig(path)
    crudConfig(path)
    interpolationDemo(path)