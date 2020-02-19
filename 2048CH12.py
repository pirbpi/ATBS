#! python3
# 2048 player : https://play2048.co/

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
url = 'https://play2048.co/'

driver.get(url)

pageElem = driver.find_element_by_tag_name('html')
while True:
    pageElem.send_keys(Keys.UP)
    pageElem.send_keys(Keys.RIGHT)
    pageElem.send_keys(Keys.DOWN)
    pageElem.send_keys(Keys.LEFT)
