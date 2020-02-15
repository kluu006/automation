from lettuce import *
from selenium import webdriver
from time import sleep

# create a new google chrome session
driver = webdriver.Chrome()

# navigate to reddit
driver.get("https://old.reddit.com/")

# finds the element for /r/all and clicks the link
r_all_link = driver.find_element_by_xpath("//a[@href='https://old.reddit.com/r/all/']")
r_all_link.click()

sleep(3)
driver.close()