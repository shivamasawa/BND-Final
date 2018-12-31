#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util

#profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
#driver = webdriver.Firefox(profile)

WEB_SITE = env_util.get_env_url()
NEWSLETTER = env_util.get_env_url() + "newsletter"
THANKS = "Oops, som"

class SubscribeTestCase(mobile_test_core.MobileTestCore):
    
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
        time.sleep(2)
        textw =  str(self.driver.find_element_by_css_selector(".content.line").text)
        thank_you = textw.encode('ascii','ignore')[:9]
        self.assertEqual(thank_you, THANKS, "Url hasn't been changed")
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SubscribeTestCase)
    unittest.TextTestRunner().run(suite)