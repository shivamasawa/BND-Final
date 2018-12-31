#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import mobile_util, env_util

WEB_SITE = env_util.get_env_url()
ARTICLE_LIST = WEB_SITE+'grow-your-business'
ARTICLE = WEB_SITE+'7898-choosing-a-digital-copier.html'

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    assert web_element.is_displayed() == True
    width = web_element.size.get('width')
    assert (width <= browser_width) and (width >= (browser_width - 40))

def verifyMobileHeader(self):
    color_bar = self.driver.find_element_by_css_selector('.sectRule.allColors.spaceB10.mqMedOn')
    verifyElementIsDisplayedAndSpansWidth(self, color_bar)
    logo = self.driver.find_element_by_css_selector('div.logo a>img.mqMedOn')
    assert logo.is_displayed() == True
    menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
    try:
        isDisplayed = menu_icon.is_displayed()
    except:
        menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
        isDisplayed = menu_icon.is_displayed()
    assert isDisplayed == True
    menu_panel = self.driver.find_element_by_css_selector('.menuPanel')
    isDisplayed = menu_panel.is_displayed()
    assert isDisplayed == False
    menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
    menu_icon.click()
    time.sleep(3)
    try:
        menu_panel = self.driver.find_element_by_css_selector('.menuPanel')
        verifyElementIsDisplayedAndSpansWidth(self, menu_panel)
    except:
        menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
        menu_icon.click() 
        menu_panel = self.driver.find_element_by_css_selector('.menuPanel')
        verifyElementIsDisplayedAndSpansWidth(self, menu_panel)
    menu_icon.click()
    time.sleep(2)
    assert menu_panel.is_displayed() == False
    
def verifyMobileFooter(self):
    social = self.driver.find_element_by_css_selector('.preFooter .inner10')
    verifyElementIsDisplayedAndSpansWidth(self, social)
    footer = self.driver.find_element_by_css_selector('footer')
    verifyElementIsDisplayedAndSpansWidth(self, footer) 
    

class MobileLayoutTestCase(mobile_test_core.MobileTestCore):
        
    def testHomepageLayout(self):
        self.driver.get(WEB_SITE)
        self.driver.refresh()
        verifyMobileHeader(self)
        featured_content = self.driver.find_element_by_css_selector('.hpFeatures.mod.topMod')
        verifyElementIsDisplayedAndSpansWidth(self, featured_content)
        start_business = self.driver.find_element_by_id('start-your-business')
        verifyElementIsDisplayedAndSpansWidth(self, start_business)
        grow_business = self.driver.find_element_by_id('grow-your-business')
        verifyElementIsDisplayedAndSpansWidth(self, grow_business)
        build_career = self.driver.find_element_by_id('build-your-career')
        verifyElementIsDisplayedAndSpansWidth(self, build_career)
        lead_your_team = self.driver.find_element_by_id('lead-your-team')
        verifyElementIsDisplayedAndSpansWidth(self, lead_your_team)
        find_solution = self.driver.find_element_by_id('find-a-solution')
        verifyElementIsDisplayedAndSpansWidth(self, find_solution)
        best_picks = self.driver.find_element_by_css_selector('.sideBar.sect-front')
        assert best_picks.is_displayed() == True
        width = best_picks.size.get('width')
        assert width == 300
        verifyMobileFooter(self)
    
    def testArticleListLayout(self):
        self.driver.get(ARTICLE_LIST)
        self.driver.refresh()
        verifyMobileHeader(self)
        breadcrumbs = self.driver.find_element_by_css_selector('.megaCrumbs.mod.topMod')
        verifyElementIsDisplayedAndSpansWidth(self, breadcrumbs)
        news_blocks = self.driver.find_elements_by_css_selector('.mod.line.newsBlock')
        for i in news_blocks:
            verifyElementIsDisplayedAndSpansWidth(self, i)
        best_picks = self.driver.find_element_by_css_selector('.sideBar.sect-front')
        assert best_picks.is_displayed() == True
        width = best_picks.size.get('width')
        assert width == 300
        verifyMobileFooter(self)
        
    def testArticleLayout(self):
        self.driver.get(ARTICLE)
        #self.driver.refresh()
        verifyMobileHeader(self)
        disclosure = self.driver.find_element_by_css_selector('.FTCdisclosure')
        verifyElementIsDisplayedAndSpansWidth(self, disclosure)
        breadcrumb = self.driver.find_element_by_css_selector('.crumbs.mod.topMod.article-crumb')
        verifyElementIsDisplayedAndSpansWidth(self, breadcrumb)
        heading = self.driver.find_element_by_css_selector('.h1.nolinks')
        verifyElementIsDisplayedAndSpansWidth(self, heading)
        by_line = self.driver.find_element_by_css_selector('.byline')
        verifyElementIsDisplayedAndSpansWidth(self, by_line)
        social_share = self.driver.find_element_by_css_selector('.shareTools.mod>ul')
        verifyElementIsDisplayedAndSpansWidth(self, social_share)
        social_share = self.driver.find_element_by_css_selector('.shareTools.mod>ul')
        verifyElementIsDisplayedAndSpansWidth(self, social_share)
        image = self.driver.find_element_by_css_selector('.articleBody img')
        verifyElementIsDisplayedAndSpansWidth(self, image)
        content = self.driver.find_element_by_css_selector('.articleBody')
        verifyElementIsDisplayedAndSpansWidth(self, content)
        author_bio = self.driver.find_element_by_css_selector('.line.authorBio')
        verifyElementIsDisplayedAndSpansWidth(self, author_bio)
        verifyMobileFooter(self)
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MobileLayoutTestCase) 
    unittest.TextTestRunner().run(suite)