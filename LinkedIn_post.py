
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class LinkedinBot:
    def __init__(self, username, password):
        """ Initialized Chromedriver, sets common urls, username and password for user """

        self.driver = webdriver.Safari()

        self.base_url = 'https://www.linkedin.com'
        self.login_url = self.base_url + '/login'

        self.username = username
        self.password = password

    def _nav(self, url):
        """Navigating url """

        self.driver.get(url)
        time.sleep(3)

    def login(self, username, password):
        """ Login to LinkedIn account """
        
        self._nav(self.login_url)
        self.driver.find_element_by_id('username').send_keys(self.username)
        self.driver.find_element_by_id('password').send_keys(self.password) #self.driver.find_element_by_xpath('//button[@data-control-urn="login-submit"]').click()
        self.driver.find_element_by_xpath("//button[contains(text(), 'Sign in')]").click()

    def post(self, text):
        """ Make a text post """
        
        self.driver.find_element_by_class_name('share-box__open').click()
        self.driver.find_element_by_class_name('mentions-texteditor__content').send_keys(text)
        self.driver.find_element_by_class_name('share-actions__primary-action').click()
    



if __name__ == '__main__':

    username = ''
    password = ''
    post_text = 'this is s trial post'
   

    bot = LinkedinBot(username, password)
    bot.login(username, password)
    bot.post(post_text)
    
