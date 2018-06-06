from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os

# from https://github.com/pyzzled/selenium/blob/master/headless_browser/headless.py
# instantiate a chrome options object so you can set the size and headless preference
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")
# download the chrome driver from https://sites.google.com/a/chromium.org/chromedriver/downloads and put it in the
# current directory
chrome_driver = os.getcwd() +"/chromedriver"
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

def namer():
    pageName = driver.execute_script("return _satellite.getVar('pageName')")
    print(pageName)
    return pageName
    
def selector(css):
    return driver.execute_script("document.getElementsByClassName({})[0].click()".format(css_class))

def full(css,t):
    selector(css)
    time.sleep(t)
    namer()

def filler(css,amount):
    inputElement = driver.find_element_by_name(css)
    inputElement.send_keys(amount)
    inputElemen
