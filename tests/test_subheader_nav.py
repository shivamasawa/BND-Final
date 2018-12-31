import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util, webdriver_util

WEB_SITE = env_util.get_env_url()
START = WEB_SITE+'start-your-business'
START_BEST = WEB_SITE+'7638-best-background-check-services.html'
START_ARTICLE = WEB_SITE+'7623-businesses-for-sale.html'
GROW = WEB_SITE+'grow-your-business'
BUILD = WEB_SITE+'build-your-career'
LEAD = WEB_SITE+'lead-your-team'
FIND = WEB_SITE+'find-a-solution'
ARTICLE = WEB_SITE+'7400-putting-apple-pay-to-work-and-how-you-can-too.html'
    
def verifySubNavigation(self, expected_color, browser_name):
        sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
#        nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.bg'+str(nav_number))
        self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
        nav_links = self.driver.find_elements_by_css_selector('.altNavList.line.mqMedOff .subItem>a')
        for link in nav_links:
            self.assertTrue(link.is_displayed(), 'sub nav link is not displayed')
        sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
#        nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
        sub_nav_color = sub_nav.value_of_css_property('background-color')
        sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
        self.assertEquals(sub_nav_color,sub_nav_bar_color, 'nav bar color and color behind nav links do not match')
        self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
        side_ads_css = '#ctMedia'
        if(webdriver_util.is_element_present(self.driver, side_ads_css)):
            if("chrome" or "headless" in browser_name):
                expected_color = u'rgba(0, 0, 0, 0)'
            else:
                expected_color = u'rgb(0, 0, 0)'
            self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')

class SubheaderTestCase(test_core.TestCore):

    def testStartBusinessPage(self):
        self.driver.get(START)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(0, 83, 186, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(0, 83, 186)', browser_name)
        
    def testStartBusinessBestPick(self):
        self.driver.get(START_BEST)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(23, 166, 255, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(23, 166, 255)', browser_name)
        
    def testStartBusinessArticle(self):
        self.driver.get(START_ARTICLE)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(0, 83, 186, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(0, 83, 186)', browser_name)
        
    def testGrowBusiness(self):
        self.driver.get(GROW)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(205, 0, 93, 1)', browser_name)
        else:
           verifySubNavigation(self, u'rgb(205, 0, 93)', browser_name) 
        
    def testBuildCareer(self):
        self.driver.get(BUILD)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(0, 205, 183, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(0, 205, 183)', browser_name)
        
    def testLeadTeam(self):
        self.driver.get(LEAD)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(255, 93, 21, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(255, 93, 21)', browser_name)
        
    def testFindSolution(self):
        self.driver.get(FIND)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(23, 166, 255, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(23, 166, 255)', browser_name)
        
    def testArticle(self):
        self.driver.get(ARTICLE)
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            verifySubNavigation(self, u'rgba(205, 0, 93, 1)', browser_name)
        else:
            verifySubNavigation(self, u'rgb(205, 0, 93)', browser_name)
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SubheaderTestCase)
    unittest.TextTestRunner().run(suite)