#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, webdriver_util

WEB_SITE = env_util.get_env_url() + "8193-working-moms-stress.html"
ONE = "Build Your Career"
TWO = "Work-Life Balance"
AUTHOR = "Brittney Morgan, Business News Daily Contributing Write"
TIME_STAMP = """July 14, 2015 09:23 am EST"""
YOUMAYLIKE = "You May Also like"

class ArticleTestCase(mobile_test_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(ArticleTestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
        try:
            driver.get(WEB_SITE)
        except Exception as e:
            driver.quit()
            raise e
      
    def testCrumb(self):
        lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child").text
        lv_one = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:first-child").text
        self.assertEquals(lv_one, ONE, "One {0} doesn't match the {1}".format(lv_one, ONE))
        self.assertEquals(lv_two, TWO, "Two {0} doesn't match the {1}".format(lv_two, TWO))
        
    def testSubNavigation(self):
        if('phone' not in self.device_name):
            sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
            nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.bg3')
            self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
            nav_links = self.driver.find_elements_by_css_selector('.altNavList.line.bg3 .subItem>a')
            for link in nav_links:
                self.assertTrue(link.is_displayed(), 'sub nav link is not displayed')
            sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
            nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
            sub_nav_color = sub_nav.value_of_css_property('background-color')
            sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
            self.assertEquals(nav_link_color, sub_nav_color, 'nav bar color and color behind nav links do not match')
            expected_color = u'rgba(0, 205, 183, 1)'
            self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
            side_ads_css = '#ctMedia'
            if(webdriver_util.is_element_present(self.driver, side_ads_css)):
                expected_color = u'rgba(0, 0, 0, 0)'
                self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')
            else:
                self.assertEqual(sub_nav_color, sub_nav_bar_color, 'Extended bar color is not correct')
   
    
    def testTimestamp(self):
        author = self.driver.find_element_by_class_name("author").text
        time_stamp = self.driver.find_element_by_css_selector(".byline time").text
        self.assertEquals(author, AUTHOR, "author {0} doesn't match the {1}".format(author, AUTHOR))
        self.assertEquals(time_stamp, TIME_STAMP, "Time {0} doesn't match the {1}".format(time_stamp, TIME_STAMP))
       
    def testYouMayAlsoLike(self):    
        yuomaylike = self.driver.find_element_by_css_selector(".sideBar div").text 
        self.assertEquals(yuomaylike.lower(), YOUMAYLIKE.lower(), "text {0} doesn't match the {1}".format(yuomaylike, YOUMAYLIKE))
        
       
    def testAnother(self):
        lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child>a")
        color = lv_two.value_of_css_property("color")
        self.assertEqual("rgba(0, 126, 204, 1)", color, "Bread crumps color was changed")
        
#    def testImageAlt(self):
#        h1 = self.driver.find_element_by_css_selector("h1")
#        h1_text = h1.text
#        image = self.driver.find_element_by_css_selector(".magnify-wrapper>img")
#        img_alt = image.get_attribute("alt")
#        self.assertNotEqual(h1_text, img_alt, "H1 and image alt are the same")
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ArticleTestCase)
    unittest.TextTestRunner().run(suite)
