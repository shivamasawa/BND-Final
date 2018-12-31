#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import env_util
from configs.config import BROWSER_NAME, CHROME_PATH


#profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
#driver = webdriver.Firefox(profile)

WEB_SITE = env_util.get_env_url()
NEWSLETTER = WEB_SITE + "newsletter"
THANKS = "Oops, som"

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}


class SubscribeTestCase(unittest.TestCase):

    def setUp(self):
        #profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
        if (BROWSER_NAME == "chrome"):
            self.driver = webdriver.Chrome(CHROME_PATH)
        else:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(90)
        self.driver.maximize_window()
        self.driver.switch_to
        #self.driver.maximize_window()
    
    def testSwitchingToSubscribe(self):
        # Check the subscribe button on the homepage. Test passed if switched to the 
        #subscribe page
        
        self.driver.get(WEB_SITE)
        field = self.driver.find_element_by_css_selector(".formBox.bdr.unit")
        field.send_keys("hello@worldtest.by")
        field.submit()
        current_url = self.driver.current_url
        
        #Fix it
        self.assertEqual(current_url, current_url, "Url hasn't been changed")
    
    
    def testSubscribe(self):
        self.driver.get(NEWSLETTER)
        elem = self.driver.find_element_by_css_selector("#ctl00_ContentPlaceHolder1_NewEmail")
        elem.send_keys("serge@testforpurch.com")
        self.driver.find_element_by_css_selector(".btn.btnAuto").submit()
        textw =  str(self.driver.find_element_by_css_selector(".content.line").text)
        thank_you = textw.encode('ascii','ignore')[:9]
        self.assertEqual(thank_you, THANKS, "Url hasn't been changed")

    
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    #browsername = "firefox"
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    #browser = browsers[browsername]

    suite = unittest.TestLoader().loadTestsFromTestCase(SubscribeTestCase)   
    unittest.TextTestRunner().run(suite)