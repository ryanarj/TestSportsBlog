import os
from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "/Users/ryanarjun/ChromeDriver/chromedriver")
Instance = None


def initialize():
    global Instance
    Instance = webdriver.Chrome(DRIVER_BIN)
    Instance.implicitly_wait(5)
    return Instance


def close_driver():
    global Instance
    Instance.quit()
