from lettuce import *
from time import sleep
from selenium import webdriver
import driver


@before.all
def set_browser():
    # create a new google chrome session
    driver.driver = webdriver.Chrome()
    # navigate to reddit
    driver.driver.get("https://old.reddit.com/")


@step('I click on r_all')
def click_r_all(step):
    # finds the element for /r/all and clicks the link
    r_all_link = driver.driver.find_element_by_xpath("//a[@href='https://old.reddit.com/r/all/']")
    r_all_link.click()


@step('I navigate to r_all')
def navigate_r_all(step):
    # validate if on /r/all
    assert driver.driver.current_url == "https://old.reddit.com/r/all/", driver.driver.current_url


@after.all
def close_browser(step):
    sleep(3)
    driver.driver.close()
