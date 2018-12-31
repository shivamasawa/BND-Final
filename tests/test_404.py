#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util

# profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
# driver = webdriver.Firefox(profile)


WEB_SITE = env_util.get_env_url() + "TEST6891-moms-work-from-home-jobs.html"
browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}


class F04TestCase(test_core.TestCore):
    
    @classmethod
    def setUpClass(cls):
        super(F04TestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        try:
            driver.get(WEB_SITE)
        except Exception as e:
            driver.quit()
            raise e
      
    def testPresentsOf404(self):
        text_alert = self.driver.find_element_by_class_name("alert").text 
        self.assert_(text_alert, "We’re sorry.")
    
    def testCSS(self):
        color = text_alert = self.driver.find_element_by_class_name("alert").value_of_css_property("color")
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            self.assertEqual(color, "rgba(211, 102, 29, 1)", "Color doesn't match")
        else:
            self.assertEqual(color, "rgb(211, 102, 29)", "Color doesn't match")
    
    def testCSS2(self):
        size = text_alert = self.driver.find_element_by_class_name("h1").value_of_css_property("font-size")
        self.assertEqual(size, "56px", "CSS has been changed. Check the 404 page")

    
if __name__ == "__main__":
    browsername = "firefox"
    if len(sys.argv) == 2:
        browsername = sys.argv[1].lower()
    browser = browsers[browsername]

    suite = unittest.TestLoader().loadTestsFromTestCase(F04TestCase)
    unittest.TextTestRunner().run(suite)
