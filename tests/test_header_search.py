#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import time 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import env_util, webdriver_util
from configs.config import CHROME_PATH, FF_PATH, CHROME_BETA_BINARY, EDGE_PATH, HEADLESS_CHROME_PATH


WEB_SITE = env_util.get_env_url()
ARTICLE_LIST = WEB_SITE+'grow-your-business'
ARTICLE = WEB_SITE+'7898-choosing-a-digital-copier.html'

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}

def verifySearch(self):
        browser_name = env_util.get_browser()
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(browser_name == "safari"):
            search_icon.click()
        else:
            webdriver_util.hover(self.driver, search_icon)
        time.sleep(3)
        search = self.driver.find_element_by_css_selector('.searchPanel')
        assert search.is_displayed() == True
        position = search.location
        y_pos = position.get('y')
        assert y_pos == 81.0
        
class HeaderSearchTestCase(unittest.TestCase):
    
    def setUp(self):
        # profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
        browser_name = env_util.get_browser();
        if(browser_name == 'headless'):
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            self.driver = webdriver.Chrome(executable_path=HEADLESS_CHROME_PATH, chrome_options=options)
        elif (browser_name == "chrome"):
            self.driver = webdriver.Chrome(CHROME_PATH)
        elif (browser_name == "chrome_beta"):
            options = webdriver.ChromeOptions()
            options.binary_location = CHROME_BETA_BINARY
            self.driver = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=options)
        elif (browser_name == "firefox"):
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            self.driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=FF_PATH)
        elif (browser_name == "safari"):
            self.driver = webdriver.Safari()
        elif (browser_name == "edge"):
            self.driver = webdriver.Edge(EDGE_PATH)
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(90)
        self.driver.maximize_window()
        self.driver.switch_to
        # self.driver.maximize_window()
        
    def testHomepageSearch(self):
        self.driver.get(WEB_SITE)
        verifySearch(self)
        
    def testArticleListSearch(self):
        self.driver.get(ARTICLE_LIST)
        verifySearch(self)
    
    def testArticleSearch(self):
        self.driver.get(ARTICLE)
        verifySearch(self)
        
    def tearDown(self):
        self.driver.quit()
        
        
if __name__ == "__main__":
    #browsername = "firefox"
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    #browser = browsers[browsername]
    suite = unittest.TestLoader().loadTestsFromTestCase(HeaderSearchTestCase)  
    unittest.TextTestRunner().run(suite)
        