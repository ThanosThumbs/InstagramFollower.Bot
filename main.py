from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium webdriver.support import expected_conditions
import time

url = 'https://www.instagram.com/login/'

SIMILAR_ACCOUNT = marvel
USERNAME = OLAKUNLEADEKOYA@ICLOUD.COM
PASSWORD = SHERIDAN211


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)


    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


bot = InstaFollower
bot.login()
bot.find_followers()
bot.follow()
