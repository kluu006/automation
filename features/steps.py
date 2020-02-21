from lettuce import *
from time import sleep
from selenium import webdriver
import driver
import subreddit
from selenium.common.exceptions import NoSuchElementException


@before.all
def set_browser():
    # create a new google chrome session
    driver.driver = webdriver.Chrome()
    # navigate to reddit
    driver.driver.get("https://old.reddit.com/")
    driver.driver.maximize_window()


@step('I click on r_all')
def click_r_all(step):
    # finds the element for /r/all and clicks the link
    r_all_link = driver.driver.find_element_by_xpath("//a[@href='https://old.reddit.com/r/all/']")
    r_all_link.click()


@step('I am on r_all')
def navigate_r_all(step):
    # validate if on /r/all
    assert driver.driver.current_url == "https://old.reddit.com/r/all/", driver.driver.current_url


@step('I have the following (\S+) subreddit')
def have_the_subreddits(step, sub):
    subreddit.name = sub


@step('I click on (\S+) subreddit')
def click_subreddit(step, sub):
    # finds the element for the subreddit and clicks the link
    try:
        link = driver.driver.find_element_by_xpath("//a[@href='https://old.reddit.com/r/%s/']" % sub)
        link.click()
    except NoSuchElementException:
        raise Exception("Element does not exist to be clicked.")


@step('I navigate to (\S+) subreddit')
def navigate_to_subreddit(step, sub):
    # validate if on subreddit
    assert driver.driver.current_url == "https://old.reddit.com/r/%s/" % subreddit.name, driver.driver.current_url


@step('Then I click on the header image')
def click_on_header_image(step):
    # click on the header image in the top banner
    try:
        image = driver.driver.find_element_by_id("header-img-a")

        image.click()
    except NoSuchElementException:
        raise Exception("Element does not exist to be clicked.")


@step('I am on the home page')
def navigate_to_home_page(step):
    # validate if on the home page
    assert driver.driver.current_url == "https://old.reddit.com/", driver.driver.current_url


@after.all
def close_browser(step):
    sleep(3)
    driver.driver.close()
