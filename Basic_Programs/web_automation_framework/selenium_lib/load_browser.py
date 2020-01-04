from selenium import webdriver
from time import sleep
from os import environ
from selenium.webdriver.firefox.options import Options
def initialize_browser(browser):
    options = Options().add_argument('--disable extension--')
    if browser=='Firefox':

        d=webdriver.Firefox(executable_path="G:\\AutomationSoftware\\geckodriver-v0.22.0-win64\\geckodriver.exe",capabilities=
{'accept_insecure_certs':True},firefox_options=options)
    if browser == 'Chrome':
        d=webdriver.Chrome(executable_path="G:\\AutomationSoftware\\chromedriver_win32\\chromedriver.exe")
                              # capabilities=
                              # {'accept_insecure_certs': True}, chrome_options=options)

    return d




