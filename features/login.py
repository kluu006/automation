from lettuce import *
from selenium import webdriver
import driver
import subreddit
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import user
from time import sleep

@step('I have a valid username and password')
def valid_credentials(step):
    # Read from text file the credentials of the test user
    # Removes trailing newline character
    f = open("features/credentials.txt", "r")
    user.username = f.readline().rstrip()
    user.password = f.readline().rstrip()


@step('I click the username form and enter username')
def click_username_form_and_enter_username(step):
    try:
        username_form = driver.driver.find_element_by_xpath("//input[@name='user']")
        username_form.send_keys(user.username)
    except NoSuchElementException:
        raise Exception("Element does not exist.")


@step('I click the password form and enter password')
def click_password_form_and_enter_password(step):
    try:
        password_form = driver.driver.find_element_by_xpath("//input[@name='passwd']")
        password_form.send_keys(user.password)
    except NoSuchElementException:
        raise Exception("Element does not exist.")


@step('I click the login button')
def click_login_button(step):
    try:
        login_button = driver.driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
    except NoSuchElementException:
        raise Exception("Element does not exist.")


@step('I am logged in')
def verify_logged_in(step):
    sleep(3)
    try:
        username = driver.driver.find_element_by_xpath("//span[@class='user']/a")
        displayed_username = username.text
        assert displayed_username == user.username, displayed_username
    except NoSuchElementException:
        raise Exception("User is not logged in.")


