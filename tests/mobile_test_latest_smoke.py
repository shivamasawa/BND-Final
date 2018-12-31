#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
import sys
import os
from datetime import date, timedelta
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util #, ad_util

WEB_SITE = env_util.get_env_url()
COUNTDOWNS = "Countdown"
IMAGE_ALBUM = "Image Album"
REFERENCE = "Reference" 
LATEST = WEB_SITE + "latest"
NEWSLETTER = WEB_SITE + "newsletter"
THANKS = "Thank you"

class LatestTestCase(mobile_test_core.MobileTestCore):
    
    def testSwitchingToLatest(self):
        self.driver.get(WEB_SITE)
        time.sleep(30)
        field = self.driver.find_element_by_css_selector(".hpLatestHeadlines")
        self.driver.execute_script("return arguments[0].scrollIntoView();", field)
        field.click()
        current_url = self.driver.current_url
        #print current_url 
    
    def testRecentNews(self):
        self.driver.get(LATEST)
        #print time.strftime("%B %d, %Y")
        today = time.strftime("%B %d, %Y")
        full_text = self.driver.find_element_by_css_selector(".date-posted").text
        full_text.encode('ascii','ignore')
        i = full_text.find(" | ") 
        #print full_text[:i]
        date_from_page = full_text[:i]
        #Check that any recent news were published today.test can fail on Monday's morning .
        #More complicated logic should be applied 
        try:
            self.assertEqual(date_from_page, today, "Latest wasn't updated today. It COULD be a problem")
        except:
            yesterday = date.today() - timedelta(1)
            yesterday = yesterday.strftime("%B %d, %Y")
            self.assertEqual(date_from_page, yesterday, "Latest wasn't updated today or yesterday. It COULD be a problem")
        
    def testFilterTypeCountdown(self):
        device_name = mobile_util.get_device_name()
        self.driver.get(LATEST)
        #ad_util.verifyAdLoadsAndClose(self.driver)
        if(device_name.__contains__("phone")):
            self.driver.find_element_by_css_selector(".filter-label.mqMedOn").click()
        elem = self.driver.find_element_by_css_selector(".filter-list li:nth-of-type(3) a")
        def hover(elem):
            hov = ActionChains(self.driver).move_to_element(elem)
            hov.perform()   
        #self.driver.find_element_by_css_selector(".pagetype-type.filter-select").click()
        elem.click()
        time.sleep(3)
        full_text_all = self.driver.find_elements_by_css_selector(".date-posted")
        for full_text in full_text_all:
            text_value = full_text.text
            content_type =  text_value[text_value.find(" | ") + 3:]
            self.assertEqual(content_type, COUNTDOWNS, "Content not valid")
            
    def testFilterTypeReference(self):
        device_name = mobile_util.get_device_name()
        self.driver.get(LATEST)
        #ad_util.verifyAdLoadsAndClose(self.driver)
        if(device_name.__contains__("phone")):
            self.driver.find_element_by_css_selector(".filter-label.mqMedOn").click()
        elem = self.driver.find_element_by_css_selector(".filter-list li:nth-of-type(5) a")
        def hover(elem):
            hov = ActionChains(self.driver).move_to_element(elem)
            hov.perform()   
        #self.driver.find_element_by_css_selector(".pagetype-type.filter-select").click()
        elem.click()
        time.sleep(3)
        full_text_all = self.driver.find_elements_by_css_selector(".date-posted")
        for full_text in full_text_all:
            text_value = full_text.text
            content_type =  text_value[text_value.find(" | ") + 3:]
            self.assertEqual(content_type, REFERENCE, "Content not valid")        
   
    def testSecondPage(self):
        self.driver.get(LATEST)
        #ad_util.verifyAdLoadsAndClose(self.driver)
        elem = self.driver.find_element_by_xpath("//section/div[2]/div/section/div/a[3]")
        elem.click()
        time.sleep(2)
        current_url = self.driver.current_url
        second_page = LATEST + "/2"
        #print "THe current url is {0}, and latest is {1}".format(current_url, second_page) 
        self.assertEqual(current_url, second_page, "Didn't change the page {0} doesn't match \n {1}".format(current_url, second_page))      
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LatestTestCase)
    unittest.TextTestRunner().run(suite)