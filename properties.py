import configparser
import os


def get_properties_from_ini(filepath):
    if not os.path.exists(filepath):
        create_config(filepath)

    config = configparser.ConfigParser()
    config.read(filepath)
    return config


def create_config(path):
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "username", "")
    config.set("Settings", "password", "")
    config.set("Settings", "api_key", "")
    config.set("Settings", "urls", "")

    with open(path, "w") as config_file:
        config.write(config_file)


settings = get_properties_from_ini('settings.ini')['Settings']