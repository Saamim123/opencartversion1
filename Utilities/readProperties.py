import configparser
import os

config=configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir)+'\\configrations\\config.ini')

class ReadConfig:
    @staticmethod
    def getApplicationURl():
        url = config.get('CommonInfo','baseurl')
        return url

    @staticmethod
    def getemail():
        email=config.get('CommonInfo','Email')
        return email

    @staticmethod
    def getpassword():
        password=config.get('CommonInfo','Password')
        return password



