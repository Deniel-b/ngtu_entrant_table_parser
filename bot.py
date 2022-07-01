import telebot
import configparser


class My_Bot():
    def __init__(self):
        super(My_Bot, self).__init__()
        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')
        self.TOKEN = self.config['bot_settings']['token']



