#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util

WEB_SITE = env_util.get_env_url()
ARTICLE = "6974-women-working-vintage-photos.html"
LEADIMAGE = "3-small-business-start-up-finance-options.html"
ARTICLESMALL = "6860-test-drive-job-candidates.html"
WEB_ARTICLE = WEB_SITE + ARTICLE
credit_text = "Credit: Photos via the Library of Congress on Flickr."
device_name = ""


class CreditsTestCase(mobile_test_core.MobileTestCore):        
      
    def testPresentsOfgot_credits(self):
        self.driver.get(WEB_ARTICLE)
        got_credits = self.driver.find_element_by_class_name("thumb-credit").text
        self.assertEqual(got_credits, credit_text, "Got the {0}, expected is {1}".format(got_credits, credit_text))  
        
    def testCSS(self):
        WEB_SITE_ = WEB_SITE + ARTICLESMALL
        self.driver.get(WEB_SITE_)
        got_credits = self.driver.find_element_by_class_name("thumb-credit").text
        credit_text = "Credit: OPOLJA/Shutterstock"
        self.assertEqual(got_credits, credit_text, "Got the {0}, expected is {1}".format(got_credits, credit_text))
    
    def testCSS2(self):
        WEB_SITE_ = WEB_SITE + LEADIMAGE
        self.driver.get(WEB_SITE_)
        got_credits = self.driver.find_element_by_class_name("thumb-credit").text
        credit_text = "Credit: Dreamstime"
        self.assertEqual(got_credits, credit_text, "Got the {0}, expected is {1}".format(got_credits, credit_text))
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CreditsTestCase)
    unittest.TextTestRunner().run(suite)