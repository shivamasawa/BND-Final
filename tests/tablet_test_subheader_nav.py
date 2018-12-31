import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, webdriver_util

WEB_SITE = env_util.get_env_url()
START = WEB_SITE+'start-your-business'
START_BEST = WEB_SITE+'7638-best-background-check-services.html'
START_ARTICLE = WEB_SITE+'7623-businesses-for-sale.html'
GROW = WEB_SITE+'grow-your-business'
BUILD = WEB_SITE+'build-your-career'
LEAD = WEB_SITE+'lead-your-team'
FIND = WEB_SITE+'find-a-solution'

def verifySubNavigation(self, nav_number, expected_color):
        sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
        nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.bg'+str(nav_number))
        self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
        nav_links = self.driver.find_elements_by_css_selector('.altNavList.line.bg'+str(nav_number)+' .subItem>a')
        for link in nav_links:
            self.assertTrue(link.is_displayed(), 'sub nav link is not displayed')
        sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
        nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
        sub_nav_color = sub_nav.value_of_css_property('background-color')
        sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
        self.assertEquals(nav_link_color, sub_nav_color, 'nav bar color and color behind nav links do not match')
        self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
        side_ads_css = '#ctMedia'
        if(webdriver_util.is_element_present(self.driver, side_ads_css)):
            expected_color = u'rgba(0, 0, 0, 0)'
            self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')
        else:
            self.assertEqual(sub_nav_color, sub_nav_bar_color, 'Extended bar color is not correct')

class TabletSubheaderTestCase(mobile_test_core.MobileTestCore):

    def testStartBusinessPage(self):
        self.driver.get(START)
        verifySubNavigation(self, 1, u'rgba(0, 83, 186, 1)')
        
    def testStartBusinessBestPick(self):
        self.driver.get(START_BEST)
        verifySubNavigation(self, 5, u'rgba(23, 166, 255, 1)')
        
    def testStartBusinessArticle(self):
        self.driver.get(START_ARTICLE)
        verifySubNavigation(self, 1, u'rgba(0, 83, 186, 1)')
        
    def testGrowBusiness(self):
        self.driver.get(GROW)
        verifySubNavigation(self, 2, u'rgba(205, 0, 93, 1)')
        
    def testBuildCareer(self):
        self.driver.get(BUILD)
        verifySubNavigation(self, 3, u'rgba(0, 205, 183, 1)')
        
    def testLeadTeam(self):
        self.driver.get(LEAD)
        verifySubNavigation(self, 4, u'rgba(255, 93, 21, 1)')
        
    def testFindSolution(self):
        self.driver.get(FIND)
        verifySubNavigation(self, 5, u'rgba(23, 166, 255, 1)')
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TabletSubheaderTestCase)
    unittest.TextTestRunner().run(suite)