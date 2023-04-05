import configparser
import os
from pathlib import Path
import configparser

#path = Path(__file__)
#ROOT_DIR = path.parent.absolute()
#config_path = os.path.join(ROOT_DIR, "config.ini")

config = configparser.ConfigParser()
config.read("C:\\Users\APOGEE\\PycharmProjects\\noncommerce\\confriguation\\config.ini")

#config = configparser.RawConfigParser()
#config.read("Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
