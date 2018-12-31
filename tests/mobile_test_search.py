#!/usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
from selenium.webdriver.common.keys import Keys
import time 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util

WEB_SITE = env_util.get_env_url()
SEARCH_URL = WEB_SITE + "search?q=hello+world"
TEXT_UN = "https://www.businessnewsdaily.com/8633-business-meeting-mistakes.html"

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    assert web_element.is_displayed() == True
    width = web_element.size.get('width')
    if('phone' in self.device_name):
        self.assertTrue((width <= browser_width) and (width >= (browser_width - 75)), "Actual width: "+str(width)+", Expected width between "+str(browser_width-75)+" and "+str(browser_width))
    else:
        if('tablet' in self.device_name):
            self.assertTrue((width <= browser_width) and (width >= (browser_width - 150)), "Actual width: "+str(width)+", Expected width between "+str(browser_width-150)+" and "+str(browser_width))
        else:
            self.assertTrue((width >= browser_width), "Actual width: "+str(width)+", Expected width greater than "+str(browser_width))

class SearchTestCase(mobile_test_core.MobileTestCore):
    
    def testFindSearch(self):
        self.driver.get(WEB_SITE)
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(self.device_name.__contains__('ipad') or self.device_name.__contains__('tablet')):
            if(self.device_name.__contains__('ipad')):
                mobile_util.tap_webview_element_with_offset(self.driver, self.device_name, search_icon, 10)
            else:
                search_icon.click()
        else:
            self.driver.execute_script('window.scrollTo(0,0)')
            menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
            menu_icon.click()
        time.sleep(1)
        self.driver.execute_script('window.scrollTo(0,0)')
        search = self.driver.find_element_by_css_selector('.searchPanel .searchBox input')
        search.send_keys("hello world")
        search.send_keys(Keys.RETURN)
        time.sleep(5)
        #elem2 = self.driver.find_element_by_css_selector(".searchBox input")
        #hover(elem)
        current_url = self.driver.current_url
        SEARCH_URL
        #print SEARCH_URL,"!!!!", "\n", current_url
        self.assertEqual(current_url, SEARCH_URL, "Url hasn't been changed")
        
    def testSearchUnique(self):
        self.driver.get(WEB_SITE)
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(self.device_name.__contains__('ipad') or self.device_name.__contains__('tablet')):
            if(self.device_name.__contains__('ipad')):
                mobile_util.tap_webview_element_with_offset(self.driver, self.device_name, search_icon, 10)
            else:
                search_icon.click()
        else:
            self.driver.execute_script('window.scrollTo(0,0)')
            menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
            menu_icon.click()
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,0)')
        search = self.driver.find_element_by_css_selector('.searchPanel .searchBox input')
        search.send_keys("Nicole Fallon" + Keys.RETURN)
        time.sleep(5)
        #element = self.driver.find_element_by_css_selector(".gs-image")
        #hover(element)
        a = self.driver.find_element_by_class_name("gs-image").get_attribute("data-ctorig")
        self.assertEqual(a, TEXT_UN, "Didn't get the right search result")
        
    def testMobileSearchLayout(self):
        self.driver.get(WEB_SITE)
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(self.device_name.__contains__('ipad') or self.device_name.__contains__('tablet')):
            if(self.device_name.__contains__('ipad')):
                mobile_util.tap_webview_element_with_offset(self.driver, self.device_name, search_icon, 10)
            else:
                search_icon.click()
        else:
            self.driver.execute_script('window.scrollTo(0,0)')
            menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
            menu_icon.click()
        time.sleep(2)
        self.driver.execute_script('window.scrollTo(0,0)')
        search = self.driver.find_element_by_css_selector('.searchPanel .searchBox input')
        search.send_keys("laptops" + Keys.RETURN)
        time.sleep(5)
        google_ads = self.driver.find_element_by_css_selector('.gsc-adBlock')
        verifyElementIsDisplayedAndSpansWidth(self, google_ads)
        search_result = self.driver.find_element_by_css_selector('.gsc-table-result tr')
        verifyElementIsDisplayedAndSpansWidth(self, search_result)
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SearchTestCase)
    unittest.TextTestRunner().run(suite)