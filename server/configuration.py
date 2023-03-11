from configparser import ConfigParser
from os import path

def get_configuration():
    # TODO Create missing config
    configuration = ConfigParser()

    # TODO Check for file existence
    configuration.read(path.join(path.dirname(__file__), 'configuration.ini'))

    return configuration

