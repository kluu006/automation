from lettuce import *
from selenium import webdriver
import driver
import subreddit
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import user
from time import sleep
from lettuce import world


@step('I click on a post')
def click_first_post(step):
    sleep(3)
    try:
        posts = world.Posts()
        first_post = posts.posts[0]
        # Takes the title name of the post in the post table to compare with the title of the post when viewing the post
        world.curr_post = first_post.find_element_by_xpath("//a[@data-event-action='title']").text
        # Clicks the comments instead to view the post since the title may lead to a non-reddit url
        first_post.find_element_by_xpath("//a[@data-event-action='comments']").click()
        sleep(3)
    except NoSuchElementException:
        raise Exception("Element does not exist to be clicked.")


@step('I view the post')
def verify_view_post(step):
    assert world.curr_post == driver.driver.find_element_by_xpath("//a[@data-event-action='title']").text,\
        "The title of the posts in the post table and the title of the post when viewing the post are not the same."
    assert len(driver.driver.find_elements_by_xpath("//a[@data-event-action='title']")) == 1,\
        "Did not click on the comments."
