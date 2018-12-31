#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util, webdriver_util

# profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
# driver = webdriver.Firefox(profile)

WEB_SITE = env_util.get_env_url() + "8193-working-moms-stress.html"
ONE = "Build Your Career"
TWO = "Work-Life Balance"
AUTHOR = "Brittney Morgan, Business News Daily Contributing Writer"
TIME_STAMP = """July 14, 2015 09:23 am EST"""
YOUMAYLIKE = "You May Also like"

browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}


class ArticleTestCase(test_core.TestCore):
    
    @classmethod
    def setUpClass(cls):
        super(ArticleTestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        try:
            driver.get(WEB_SITE)
        except Exception as e:
            driver.quit()
            raise e
        
    def testSubNavigation(self):
        browser_name = env_util.get_browser()
        sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
        nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.mqMedOff')
        self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
        nav_links = self.driver.find_elements_by_css_selector('.altNavList.line.mqMedOff .subItem>a')
        for link in nav_links:
            self.assertTrue(link.is_displayed(), 'sub nav link is not displayed')
        sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
        nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
        sub_nav_color = sub_nav.value_of_css_property('background-color')
        sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
        print nav_link_color
        print sub_nav_color
#        self.assertEquals(nav_link_color, sub_nav_color, 'nav bar color and color behind nav links do not match')
        if("chrome" or "headless" in browser_name):
            expected_color = u'rgba(0, 205, 183, 1)'
        else:
            expected_color = u'rgb(0, 205, 183)'
        self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
        side_ads_css = '#ctMedia'
        if(webdriver_util.is_element_present(self.driver, side_ads_css)):
            if("chrome" or "headless" in browser_name):
                expected_color = u'rgba(0, 83, 186, 1)'
            else:
                expected_color = u'rgb(0, 83,186 )'
            self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')
        else:
            self.assertEqual(sub_nav_color, sub_nav_bar_color, 'Extended bar color is not correct')
     
      
    def testCrumb(self):
        lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child").text.strip()
        lv_one = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:first-child").text.strip()
        self.assertEquals(lv_one, ONE, "One {0} doesn't match the {1}".format(lv_one, ONE))
        self.assertEquals(lv_two, TWO, "Two {0} doesn't match the {1}".format(lv_two, TWO))
   
    
    def testTimestamp(self):
        author = self.driver.find_element_by_class_name("author").text.strip()
        time_stamp = self.driver.find_element_by_css_selector(".byline time").text.strip()
        self.assertEquals(author, AUTHOR, "author {0} doesn't match the {1}".format(author, AUTHOR))
        self.assertEquals(time_stamp, TIME_STAMP, "Time {0} doesn't match the {1}".format(time_stamp, TIME_STAMP))
       
    def testYouMayAlsoLike(self):    
        yuomaylike = self.driver.find_element_by_css_selector(".sideBar div").text 
        self.assertEquals(yuomaylike.lower(), YOUMAYLIKE.lower(), "text {0} doesn't match the {1}".format(yuomaylike, YOUMAYLIKE))
        
       
    def testAnother(self):
        lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child>a")
        color = lv_two.value_of_css_property("color")
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            self.assertEqual("rgba(0, 126, 204, 1)", color, "Bread crumbs color was changed")
        else:
            self.assertEqual("rgb(0, 126, 204)", color, "Bread crumbs color was changed")
        
#    def testImageAlt(self):
#        self.driver.get(WEB_SITE)
#        h1 = self.driver.find_element_by_css_selector("h1")
#        h1_text = h1.text
#        image = self.driver.find_element_by_css_selector(".magnify-wrapper>img")
#        img_alt = image.get_attribute("alt")
#        self.assertNotEqual(h1_text, img_alt, "H1 and image alt are the same")
    
if __name__ == "__main__":
    #browsername = "firefox"
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    #browser = browsers[browsername]

    suite = unittest.TestLoader().loadTestsFromTestCase(ArticleTestCase)
    unittest.TextTestRunner().run(suite)
