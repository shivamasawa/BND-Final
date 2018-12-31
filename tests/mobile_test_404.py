#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import env_util
from core import mobile_test_core

WEB_SITE = env_util.get_env_url() + "TEST6891-moms-work-from-home-jobs.html"

class F04TestCase(mobile_test_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(F04TestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
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
        self.assertEqual(color, "rgba(211, 102, 29, 1)", "Color doesn't match")
    
    def testCSS2(self):
        size = text_alert = self.driver.find_element_by_class_name("h1").value_of_css_property("font-size")
        self.assertEqual(size, "56px", "CSS has been changed. Check the 404 page")

    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(F04TestCase)
    unittest.TextTestRunner().run(suite)
