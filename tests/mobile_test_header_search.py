#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import time 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util

WEB_SITE = env_util.get_env_url()
ARTICLE_LIST = WEB_SITE+'grow-your-business'
ARTICLE = WEB_SITE+'7898-choosing-a-digital-copier.html'

def verifySearch(self):
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
        search = self.driver.find_element_by_css_selector('.searchPanel')
        assert search.is_displayed() == True
        position = search.location
        y_pos = position.get('y')
        if(self.device_name.__contains__('phone')):
            assert y_pos == 54.0
        else:
            assert y_pos == 81.0
            
class HeaderSearchTestCase(mobile_test_core.MobileTestCore):
        
    def testHomepageSearch(self):
        self.driver.get(WEB_SITE)
        verifySearch(self)
        
    def testArticleListSearch(self):
        self.driver.get(ARTICLE_LIST)
        verifySearch(self)
        
    def testArticleSearch(self):
        self.driver.get(ARTICLE)
        verifySearch(self)
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HeaderSearchTestCase) 
    unittest.TextTestRunner().run(suite)
        