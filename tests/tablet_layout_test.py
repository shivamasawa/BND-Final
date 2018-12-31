#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util

WEB_SITE = env_util.get_env_url()
ARTICLE_LIST = WEB_SITE+'grow-your-business'
ARTICLE = WEB_SITE+'7898-choosing-a-digital-copier.html'

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    assert web_element.is_displayed() == True
    width = web_element.size.get('width')
    if(self.device_name.__contains__('android')):
        assert width == 800
    else:
        assert (width <= browser_width) and (width >= (browser_width - 40))
    
def verifyElementIsDisplayedAndSpansSpecificWidth(self, web_element, width):
    assert web_element.is_displayed() == True
    element_width = web_element.size.get('width')
    assert element_width == width
    
def verifyElementIsDisplayedAndMinimumWidth(self, web_element, width):
    assert web_element.is_displayed() == True
    element_width = web_element.size.get('width')
    assert element_width >= width

def verifyTabletHeader(self):
    header = self.driver.find_element_by_css_selector('header.masthead.cf')
    verifyElementIsDisplayedAndSpansWidth(self, header)
    logo = self.driver.find_element_by_css_selector('div.logo a>img.mqMedOff')
    assert logo.is_displayed() == True
    site_nav = self.driver.find_element_by_css_selector('.siteNav.unit')
    assert site_nav.is_displayed() == True
    search = self.driver.find_element_by_css_selector('.iconNav.navSearch.unit.spaceR5')
    assert search.is_displayed() == True
    social_nav = self.driver.find_element_by_css_selector('.iconNav.navSocial.unit')
    assert social_nav.is_displayed() == True
    menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
    assert menu_icon.is_displayed() == False
    
def verifyAdBlock(self):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    ad_block = self.driver.find_element_by_id('ad_leaderboard')
    if(self.device_name.__contains__('android')):
        verifyElementIsDisplayedAndMinimumWidth(self, ad_block, browser_width-2)
    else:    
        verifyElementIsDisplayedAndMinimumWidth(self, ad_block, browser_width)
    
def verifyTabletFooter(self):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    pre_footer = self.driver.find_element_by_css_selector('.preFooter .inner10')
    footer = self.driver.find_element_by_css_selector('footer')
    if(self.device_name.__contains__('android')):
        verifyElementIsDisplayedAndMinimumWidth(self, pre_footer, 1000)
        verifyElementIsDisplayedAndMinimumWidth(self, footer, 1030)
    else:
        verifyElementIsDisplayedAndMinimumWidth(self, pre_footer, browser_width)
        verifyElementIsDisplayedAndMinimumWidth(self, footer, browser_width)
    

class TabletLayoutTestCase(mobile_test_core.MobileTestCore):
        
    def testHomepageLayout(self):
        self.driver.get(WEB_SITE)
        verifyTabletHeader(self)
        verifyAdBlock(self)
        best_picks = self.driver.find_element_by_css_selector('.sideBar.sect-front')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, best_picks, 300)
        width = 600
        featured_content = self.driver.find_element_by_css_selector('.hpFeatures.mod.topMod')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, featured_content, width)
        start_business = self.driver.find_element_by_id('start-your-business')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, start_business, width)
        grow_business = self.driver.find_element_by_id('grow-your-business')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, grow_business, width)
        build_career = self.driver.find_element_by_id('build-your-career')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, build_career, width)
        lead_your_team = self.driver.find_element_by_id('lead-your-team')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, lead_your_team, width)
        find_solution = self.driver.find_element_by_id('find-a-solution')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, find_solution, width)
        verifyTabletFooter(self)
    
    def testArticleListLayout(self):
        self.driver.get(ARTICLE_LIST)
        browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
        verifyTabletHeader(self)
        verifyAdBlock(self)
        sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
        verifyElementIsDisplayedAndMinimumWidth(self, sub_nav, browser_width)
        breadcrumbs = self.driver.find_element_by_css_selector('.megaCrumbs.mod.topMod')
        if(self.device_name.__contains__('android')):
            verifyElementIsDisplayedAndMinimumWidth(self, breadcrumbs, 940)
        else:
            verifyElementIsDisplayedAndMinimumWidth(self, breadcrumbs, browser_width)
        best_picks = self.driver.find_element_by_css_selector('.sideBar.sect-front')
        verifyElementIsDisplayedAndSpansSpecificWidth(self, best_picks, 300)
        news_blocks = self.driver.find_elements_by_css_selector('.mod.line.newsBlock')
        for i in news_blocks:
            verifyElementIsDisplayedAndSpansSpecificWidth(self, i, 600)
        verifyTabletFooter(self)
        
        
    def testArticleLayout(self):
        self.driver.get(ARTICLE)
        browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
        verifyTabletHeader(self)
        sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
        verifyElementIsDisplayedAndMinimumWidth(self, sub_nav, browser_width)
        disclosure = self.driver.find_element_by_css_selector('.FTCdisclosure')
        breadcrumb = self.driver.find_element_by_css_selector('.crumbs.mod.topMod.article-crumb')
        heading = self.driver.find_element_by_css_selector('.h1.nolinks')
        by_line = self.driver.find_element_by_css_selector('.byline-wrapper')
        content = self.driver.find_element_by_css_selector('.articleBody')
        author_bio = self.driver.find_element_by_css_selector('.line.authorBio')
        if(self.device_name.__contains__('android')):
            verifyElementIsDisplayedAndMinimumWidth(self, disclosure, 1000)
            verifyElementIsDisplayedAndMinimumWidth(self, breadcrumb, 1000)
            verifyElementIsDisplayedAndMinimumWidth(self, heading, 1000)
            verifyElementIsDisplayedAndMinimumWidth(self, by_line, 1000)
            verifyElementIsDisplayedAndMinimumWidth(self, content, 1000)
            verifyElementIsDisplayedAndMinimumWidth(self, author_bio, 1000)
        else:   
            verifyElementIsDisplayedAndMinimumWidth(self, disclosure, browser_width)
            verifyElementIsDisplayedAndMinimumWidth(self, breadcrumb, browser_width)
            verifyElementIsDisplayedAndMinimumWidth(self, heading, browser_width)
            verifyElementIsDisplayedAndMinimumWidth(self, by_line, browser_width)
            verifyElementIsDisplayedAndMinimumWidth(self, content, browser_width)
            verifyElementIsDisplayedAndMinimumWidth(self, author_bio, browser_width)
        image = self.driver.find_element_by_css_selector('.articleBody img')
        verifyElementIsDisplayedAndMinimumWidth(self, image, 300)     
        verifyTabletFooter(self) 
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TabletLayoutTestCase) 
    unittest.TextTestRunner().run(suite)