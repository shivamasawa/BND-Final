#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time 
import sys
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import env_util #, ad_util
from configs.config import CHROME_PATH, FF_PATH, CHROME_BETA_BINARY, EDGE_PATH, HEADLESS_CHROME_PATH

#profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
#driver = webdriver.Firefox(profile)
WEB_SITE = env_util.get_env_url()
SEARCH_URL = WEB_SITE + "search?q=hello+world"
TEXT_UN = "https://www.businessnewsdaily.com/8633-business-meeting-mistakes.html"

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}


class SearchTestCase(unittest.TestCase):
    
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
        self.browser_name = browser_name
        # self.driver.maximize_window()
        
    def testFindSerch(self):
        self.driver.get(WEB_SITE)
        #ad_util.verifyAdLoadsAndClose(self.driver)
        def hover(elem):
            hov = ActionChains(self.driver).move_to_element(elem)
            hov.perform()           
        elem = self.driver.find_element_by_css_selector(".searchIcon.fa.fa-search.circle.circleAlt")
        if(self.browser_name == "safari"):
            elem.click()
        else:
            hover(elem)
        self.driver.find_element_by_css_selector(".searchBox input").send_keys("hello world" + Keys.RETURN)
        #elem2 = self.driver.find_element_by_css_selector(".searchBox input")
        #hover(elem)
        current_url = self.driver.current_url
        SEARCH_URL
        #print SEARCH_URL,"!!!!", "\n", current_url
        try:
            self.assertEqual(current_url, SEARCH_URL, "Url hasn't been changed")
        except:
            time.sleep(2)
            current_url = self.driver.current_url
            self.assertEqual(current_url, SEARCH_URL, "Url hasn't been changed")
        
        
    def testSerheUnique(self):
        self.driver.get(WEB_SITE)
        #ad_util.verifyAdLoadsAndClose(self.driver)
        def hover(elem):
            hov = ActionChains(self.driver).move_to_element(elem)
            hov.perform()           
        elem = self.driver.find_element_by_css_selector(".searchIcon.fa.fa-search.circle.circleAlt")
        if(self.browser_name == "safari"):
            elem.click()
        else:
            hover(elem)
        self.driver.find_element_by_css_selector(".searchBox input").send_keys("Nicole Fallon" + Keys.RETURN)
        time.sleep(3)
        element = self.driver.find_element_by_css_selector(".gs-image")
        a = self.driver.find_element_by_class_name("gs-image").get_attribute("data-ctorig")
        self.assertEqual(a, TEXT_UN, "Didn't get the right search result")
        
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    #browsername = "firefox"
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    #browser = browsers[browsername]

    suite = unittest.TestLoader().loadTestsFromTestCase(SearchTestCase)  
    unittest.TextTestRunner().run(suite)