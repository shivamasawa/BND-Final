#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import datetime
import time
import sys
import os
import random
from lib2to3.tests.support import driver
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util, webdriver_util

WEB_SITE = env_util.get_env_url()
ARTICLES = ["2389-jobs-travel-lovers.html","2747-great-business-ideas.html","1646-great-business-ideas-2012.html","1999-great-business-ideas-2012.html","5126-best-jobs-introverts.html"]



DISCLAIMER_TEXT = u'Product and service reviews are conducted independently by our editorial team, but we sometimes make money when you click on links. Learn more.'
LEARN_MORE_URL = WEB_SITE+'advertising-disclosure'
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]
COMPANY_LINKS = ['About Us','Contact Us','Partner with Us','Copyright Policy','Terms of Use','Privacy Policy','Advertising Disclosure','Sitemap']
COMPANY_URLS = [WEB_SITE+'about','mailto:%20editor@business.com','https://www.business.com/partner/#overview',WEB_SITE+'copyright-policy',WEB_SITE+'terms-of-use',WEB_SITE+'privacy-policy',WEB_SITE+'advertising-disclosure',WEB_SITE+'sitemap']
NETWORK_LINKS = ["Business.com", "BuyerZone.com"]
NETWORK_URLS = ['https://www.business.com/','https://www.buyerzone.com/']
COPYRIGHT = u'Copyright © '+str(datetime.datetime.now().year)+u' All Rights Reserved.'

class CountdownTestCase(test_core.TestCore):
    
    @classmethod
    def setUpClass(cls):
        super(CountdownTestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        try:
            url = WEB_SITE+ARTICLES[random.randint(0, len(ARTICLES)-1)]
            print(url)
            driver.get(url)
        except Exception as e:
            driver.quit()
            raise e
        
    def testHeader(self):
        header = self.driver.find_element_by_css_selector('.masthead.cf')
        self.assertTrue(header.is_displayed(), 'Header is not displayed')
        bnd_logo = self.driver.find_element_by_css_selector('img.mqMedOff')
        self.assertTrue(bnd_logo.is_displayed(), 'BND logo is not displayed')
        site_nav = self.driver.find_element_by_css_selector('nav.siteNav')
        self.assertTrue(site_nav.is_displayed(), 'Site navigation is not displayed')
        header_search = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        self.assertTrue(header_search.is_displayed(), 'Header search icon is not displayed')
        fb = self.driver.find_element_by_css_selector('.navSocial .fa.fa-facebook.circle.spaceR15')
        self.assertTrue(fb.is_displayed(), 'Header facebook icon is not displayed')
        twitter = self.driver.find_element_by_css_selector('.navSocial .fa.fa-twitter.circle.spaceR15')
        self.assertTrue(twitter.is_displayed(), 'Header twitter icon is not displayed')
        linkedin = self.driver.find_element_by_css_selector('.navSocial .fa.fa-linkedin.circle.spaceR15')
        self.assertTrue(linkedin.is_displayed(), 'Header linkedin icon is not displayed')
#        instagram = self.driver.find_element_by_css_selector('.navSocial .fa.fa-instagram.circle.spaceR15')
#        self.assertTrue(instagram.is_displayed(), "Header instagram icon is not displayed")
        
    def testSearch(self):
        browser_name = env_util.get_browser()
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(browser_name == "safari"):
            search_icon.click()
        else:
            webdriver_util.hover(self.driver, search_icon)
        time.sleep(1)
        search = self.driver.find_element_by_css_selector('.searchPanel')
        assert search.is_displayed() == True
        position = search.location
        y_pos = position.get('y')
        assert y_pos == 81.0
        
    def testSubNavigation(self):
        sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
        if ('2389-jobs-travel-lovers.html' not in self.driver.current_url):
#            nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.altNavList:not(.h)')
            self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
            sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
#            nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
            sub_nav_color = sub_nav.value_of_css_property('background-color')
            sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
#            print nav_link_color
#            print sub_nav_color
            self.assertEquals(sub_nav_color, sub_nav_bar_color, 'nav bar color and color behind nav links do not match')
            browser_name = env_util.get_browser()
            if("chrome" or "headless" in browser_name):
                expected_color = u'rgba(0, 83, 186, 1)'
            else:
                expected_color = u'rgb(0, 83, 186)'
            self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
            side_ads_css = '#ctMedia'
            if(webdriver_util.is_element_present(self.driver, side_ads_css)):
                if("chrome" or "headless" in browser_name):
                    expected_color = u'rgba(0, 0, 0, 0)'
                else:
                    expected_color = u'rgba(0, 0, 0)'
                self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')
        
    def testAdDisclaimer(self):
        disclaimer = self.driver.find_element_by_css_selector('.FTCdisclosure')
        actual_text = disclaimer.text.strip()
        browser_name = env_util.get_browser()
        if(browser_name == "safari"):
            actual_text = actual_text.replace("\n              ", "")
        self.assertEquals(actual_text, DISCLAIMER_TEXT, "actual [{0}] doesn't match expected [{1}]".format(actual_text, DISCLAIMER_TEXT))
        learn_more = self.driver.find_element_by_css_selector('.FTCdisclosure>a')
        actual_text = learn_more.text.strip()
        expected_text = "Learn more."
        self.assertEquals(actual_text, expected_text, "actual [{0}] doesn't match expected [{1}]".format(actual_text, expected_text))
        learn_more_url = learn_more.get_attribute('href')
        self.assertEquals(learn_more_url, LEARN_MORE_URL, "actual [{0}] doesn't match expected [{1}]".format(learn_more_url, LEARN_MORE_URL))
        
    def testBreadCrumb(self):
        lv_one = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:first-child")
        self.assertTrue(lv_one.is_displayed(), "First breadcrumb not displayed");
        lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child")
        self.assertTrue(lv_two.is_displayed(), "Second breadcrumb is not displayed")
        lv_two_bc = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child>a")
        color = lv_two_bc.value_of_css_property("color")
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            self.assertEqual("rgba(0, 126, 204, 1)", color, "Bread crumbs color was changed")
        else:
            self.assertEqual("rgb(0, 126, 204)", color, "Bread crumbs color was changed")
    
    def testHeadline(self):
        headline = self.driver.find_element_by_css_selector('.h1.nolinks')
        self.assertTrue(headline.is_displayed(), 'Article headline is not displayed')
        
    def testByLine(self):
        author = self.driver.find_element_by_css_selector('.author')
        self.assertTrue(author.is_displayed(), 'Author is not displayed')
        date = self.driver.find_element_by_css_selector('.byline>time')
        self.assertTrue(date.is_displayed(), "'Publish date is not displayed")
        fb = self.driver.find_element_by_css_selector('.st_facebook_custom.fa.fa-facebook')
        self.assertTrue(fb.is_displayed(), 'Facebook social share icon is displayed')
        twitter = self.driver.find_element_by_css_selector('.st_twitter_custom.fa.fa-twitter')
        self.assertTrue(twitter.is_displayed(), 'Twitter social share icon is displayed')
        linkedin = self.driver.find_element_by_css_selector('.st_linkedin_custom.fa.fa-linkedin')
        self.assertTrue(linkedin.is_displayed(), 'Linkedin social share icon is displayed')
        reddit = self.driver.find_element_by_css_selector('.st_reddit_custom.fa.fa-reddit')
        self.assertTrue(reddit.is_displayed(), 'Reddit social share icon is displayed')
        stumbleupon = self.driver.find_element_by_css_selector('.st_stumbleupon_custom.fa.fa-stumbleupon')
        self.assertTrue(stumbleupon.is_displayed(), 'stumbleupon social share icon is displayed')
        more = self.driver.find_element_by_css_selector('.st_sharethis_custom.stMore')
        self.assertTrue(more.is_displayed(), 'more social share option is displayed')
        
    def testContent(self):
        tabs = self.driver.find_elements_by_css_selector('a.slideNum')
        expected_num_tabs = 2 + int(tabs[1].text)
        self.assertEquals(len(tabs), expected_num_tabs, "Expected "+str(expected_num_tabs)+" tabs but found"+str(len(tabs)))
        slides = self.driver.find_elements_by_css_selector('.multiPageItem.cycle-slide');
        left_arrow = self.driver.find_element_by_css_selector('span#prev')
        self.assertTrue(left_arrow.is_displayed(), "Left arrow not displayed")
        right_arrow = self.driver.find_element_by_css_selector('span#next')
        self.assertTrue(right_arrow.is_displayed(), "Right arrow not displayed")
        for x in range(expected_num_tabs):
            tab = tabs[x]
            try:
                self.assertTrue(tab.is_displayed(), "Tab "+str(x)+" not displayed")
            except:
                time.sleep(1)
                self.assertTrue(tab.is_displayed(), "Tab "+str(x)+" not displayed")
            slide = slides[x]
            self.assertTrue(slide.is_displayed(), "Slide "+str(x)+" not displayed")
            if(x == expected_num_tabs-1):
                last_links = slide.find_elements_by_css_selector('.slideContainer a img');
                self.assertEquals(len(last_links), 6, "Less than 6 links loaded on last slide")
            else:
                heading = slide.find_element_by_css_selector('h2')
                self.assertTrue(heading.is_displayed(), "Heading not displayed for slide "+str(x))
                thumbnail = slide.find_element_by_css_selector('figure.thumbLeft')
                self.assertTrue(thumbnail.is_displayed(), "Thumbnail not displayed for slide "+str(x))
                slide_text = slide.find_element_by_css_selector('span.slideText')
                self.assertTrue(slide_text.is_displayed(), "Slide content not displayed for slide "+str(x))
                right_arrow.click()
        
    def testAuthor(self):  
        author_name = self.driver.find_element_by_css_selector('.authorName')
        self.assertTrue(author_name.is_displayed(), "Author name not displayed")
        author_about = self.driver.find_element_by_css_selector('.authorDesc>p')
        self.assertTrue(author_about.is_displayed(), "Author about not displayed")
        author_image = self.driver.find_element_by_css_selector('img.author-thumb')
        self.assertTrue(author_image.is_displayed(), "Author image not displayed")
        author_twitter = self.driver.find_element_by_css_selector('.socialByline>a')
        self.assertTrue(author_twitter, "Author twitter not displayed")
        
    def testRelatedSection(self):
        url = self.driver.current_url
        if ("2389-jobs-travel-lovers.html" not in url):
            section = self.driver.find_element_by_css_selector('.modTitle')
            self.assertTrue(section.is_displayed(), "Section name not displayed")
            see_all = self.driver.find_element_by_css_selector('.relatedBlock a')
            self.assertTrue(see_all.is_displayed(), "See all link not displayed")
            related_sections = self.driver.find_elements_by_css_selector('.relatedTitle')
            self.assertEquals(len(related_sections), 5, "less than 5 related sections")
            for section in related_sections:
                self.assertTrue(section.is_displayed(), "At least on section is not displayed")
    
    def testFooter(self):
        sub_menus = self.driver.find_elements_by_css_selector(".unit.netLinks")
        all_url = []
        for sub_group in sub_menus:
            self.assertTrue(sub_group.is_displayed(), 'link group in footer is not displayed')
            column = []
            url_category = sub_group.find_element_by_tag_name("a").get_attribute("href")
            column.append(url_category)
            list_of_li = sub_group.find_elements_by_css_selector(".netLink")
            for i in list_of_li:
                #line_url = i.get_attribute("href")
                line_text = i.text.strip()
                #column.append(line_url)
                column.append(line_text)
            all_url.append(column)
        #print "New", all_url
        self.assertEqual(all_url, FOOTER, "Footer has been changed. URLs or Text changed")
        fb = self.driver.find_element_by_css_selector('.preFooter .fa.fa-facebook.circle.spaceR15')
        self.assertTrue(fb.is_displayed(), 'Footer facebook icon is not displayed')
        twitter = self.driver.find_element_by_css_selector('.preFooter .fa.fa-twitter.circle.spaceR15')
        self.assertTrue(twitter.is_displayed(), 'Footer twitter icon is not displayed')
        linkedin = self.driver.find_element_by_css_selector('.preFooter .fa.fa-linkedin.circle.spaceR15')
        self.assertTrue(linkedin.is_displayed(), 'Footer linkedin icon is not displayed')
        purch_logo =  self.driver.find_element_by_css_selector('.footer .mod>a>img')
        self.assertTrue(purch_logo.is_displayed(), 'Purch logo is not displayed')
        copy_right = self.driver.find_element_by_css_selector('.copyRight')
        self.assertTrue(copy_right.is_displayed(), "Copyright is not displayed")
        copyright_text = copy_right.text
        browser_name = env_util.get_browser()
        if(browser_name == "safari" or browser_name == "edge"):
            copyright_text = copyright_text.strip().replace("\n                    ", " ").replace("document.write(new Date().getFullYear());", "")
        self.assertEquals(copyright_text, COPYRIGHT, "Copyright message is not correct")
        company = self.driver.find_element_by_xpath('html/body/footer/div[1]/div/section[1]/header').text
        if(browser_name == "safari" or browser_name == "edge"):
            company = company.strip().upper()
        self.assertEquals(company, "COMPANY", "actual [{0}] doesn't match expected [{1}]".format(company, "COMPANY"))
        company_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/section[1]/ul/li/a')
        for i in range(0, len(company_links)):
            link = company_links[i]
            link_text = link.text.strip()
            self.assertEquals(link_text, COMPANY_LINKS[i], "actual [{0}] doesn't match expected [{1}]".format(link_text, COMPANY_LINKS[i]))
            link_url = link.get_attribute('href')
            self.assertEquals(link_url, COMPANY_URLS[i], "actual [{0}] doesn't match expected [{1}]".format(link_url, COMPANY_URLS[i]))
        network = self.driver.find_element_by_xpath('html/body/footer/div[1]/div/section[2]/header').text
        if(browser_name == "safari" or browser_name == "edge"):
            network = network.strip().upper()
        self.assertEquals(network, "NETWORK", "actual [{0}] doesn't match expected [{1}]".format(network, "NETWORK"))
        network_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/section[2]/ul/li/a')
        for i in range(0, len(network_links)):
            link = network_links[i]
            link_text = link.text.strip()
            try:
                self.assertEquals(link_text, NETWORK_LINKS[i], "actual [{0}] doesn't match expected [{1}]".format(link_text, NETWORK_LINKS[i]))
            except:
                link_text = link_text.replace("  ", " ")
                self.assertEquals(link_text, NETWORK_LINKS[i], "actual [{0}] doesn't match expected [{1}]".format(link_text, NETWORK_LINKS[i]))
            link_url = link.get_attribute('href')
            self.assertEquals(link_url, NETWORK_URLS[i], "actual [{0}] doesn't match expected [{1}]".format(link_url, NETWORK_URLS[i]))
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CountdownTestCase)
    unittest.TextTestRunner().run(suite) 
        
        