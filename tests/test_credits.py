#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util

#profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
#driver = webdriver.Firefox(profile)

WEB_SITE = env_util.get_env_url()
ARTICLE = "6974-women-working-vintage-photos.html"
LEADIMAGE = "3-small-business-start-up-finance-options.html"
ARTICLESMALL = "6860-test-drive-job-candidates.html"
WEB_ARTICLE = WEB_SITE + ARTICLE
browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}
credit_text = "Credit: Photos via the Library of Congress on Flickr."


class CreditsTestCase(test_core.TestCore):
      
    def testPresentsOfgot_credits(self):
        self.driver.get(WEB_ARTICLE)
        got_credits = self.driver.find_element_by_class_name("thumb-credit").text
        self.assertEqual(got_credits, credit_text, "Got the {0}, expected is {1}".format(got_credits, credit_text))
        
    def testCSS(self):
        WEB_SITE_ = WEB_SITE + ARTICLESMALL
        self.driver.get(WEB_SITE_)
        got_credits = self.driver.find_element_by_class_name("thumb-credit").text.strip()
        credit_text = "Credit: OPOLJA/Shutterstock"
        self.assertEqual(got_credits, credit_text, "Got the {0}, expected is {1}".format(got_credits, credit_text))
    
    def testCSS2(self):
        WEB_SITE_ = WEB_SITE + LEADIMAGE
        self.driver.get(WEB_SITE_)
        got_credits = self.driver.find_element_by_class_name("thumb-credit").text.strip()
        credit_text = "Credit: Dreamstime"
        self.assertEqual(got_credits, credit_text, "Got the {0}, expected is {1}".format(got_credits, credit_text))
 
    
if __name__ == "__main__":
    #browsername = "firefox"
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    #browser = browsers[browsername]

    suite = unittest.TestLoader().loadTestsFromTestCase(CreditsTestCase)
    unittest.TextTestRunner().run(suite)