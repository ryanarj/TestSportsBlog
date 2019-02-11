from selenium import webdriver
import os


class Driver(object):
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/ryanarjun/ChromeDriver/chromedriver")

    def __init__(self, url):
        self.url = url

    def driver(self, db=DRIVER_BIN):
        browser = webdriver.Chrome(executable_path=db)
        browser.get(self.url)
        return browser
