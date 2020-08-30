from lettuce import world
from selenium.common.exceptions import NoSuchElementException
import driver


@world.absorb
class Posts:
    def __init__(self):
        self.posts = []
        self.retrieve_posts()


    def retrieve_posts(self):
        try:
            self.posts = driver.driver.find_elements_by_xpath("//div[@id='siteTable']/div[contains(@class,'thing id') "
                                                              "and not (contains(@class,'promoted'))]")
        except NoSuchElementException:
            raise Exception("Elements do not exist.")
