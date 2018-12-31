#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import datetime
import time
import sys
import os
from selenium.common.exceptions import WebDriverException
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util, webdriver_util
#env_util.envor = 'prod'
WEB_SITE = env_util.get_env_url()
SITE = WEB_SITE+'7839-best-crm-software.html'
DISCLAIMER_TEXT = u'Product and service reviews are conducted independently by our editorial team, but we sometimes make money when you click on links. Learn more.'
LEARN_MORE_URL = 'https://purch.com/advertising-disclosure/'
ONE = 'Find A Solution'
TWO = 'Marketing Solutions'
HEADLINE = 'Best CRM Software 2018'
PROD_HEADLINE = 'Best CRM Software 2018'
AUTHOR = 'Mona Bushnell'
PROD_AUTHOR = 'Mona Bushnell'
PUBLISH_DATE = 'August 7, 2018'
PROD_PUBLISH_DATE = 'August 7, 2018'
FIRST_HEADER = 'Our Best Picks'
FULLLIST_HEADER = 'Full List of CRM Software'
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]
COMPANY_LINKS = ['About Us','Contact Us','Partner with Us','Copyright Policy','Terms of Use','Privacy Policy','Advertising Disclosure','Sitemap']
COMPANY_URLS = [WEB_SITE+'about','mailto:%20editor@business.com','https://www.business.com/partner/#overview',WEB_SITE+'copyright-policy',WEB_SITE+'terms-of-use',WEB_SITE+'privacy-policy',WEB_SITE+'advertising-disclosure',WEB_SITE+'sitemap']
NETWORK_LINKS = ["Business.com", "BuyerZone.com"]
NETWORK_URLS = ['https://www.business.com/','https://www.buyerzone.com/']
COPYRIGHT = u'Copyright © '+str(datetime.datetime.now().year)+u' All Rights Reserved.'

class OptimizedTemplateTestCase(test_core.TestCore):
    
    @classmethod
    def setUpClass(cls):
        super(OptimizedTemplateTestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        try:
            driver.get(SITE)
        except Exception as e:
            driver.quit()
            raise e
        
    def testHeader(self):
        header = self.driver.find_element_by_css_selector('.masthead.cf')
        self.assertTrue(header.is_displayed(), 'Header is not displayed')
        bnd_logo = self.driver.find_element_by_css_selector('.logo.unit')
        self.assertTrue(bnd_logo.is_displayed(), 'BND logo is not displayed')
        site_nav = self.driver.find_element_by_css_selector('.siteNav.unit')
        self.assertTrue(site_nav.is_displayed(), 'Site navigation is not displayed')
        header_search = self.driver.find_element_by_css_selector('.iconNav.navSearch.unit.spaceR5')
        self.assertTrue(header_search.is_displayed(), 'Header search icon is not displayed')
        fb = self.driver.find_element_by_css_selector('.iconNav.navSocial.unit .fa.fa-facebook.circle.spaceR15')
        self.assertTrue(fb.is_displayed(), 'Header facebook icon is not displayed')
        twitter = self.driver.find_element_by_css_selector('.iconNav.navSocial.unit .fa.fa-twitter.circle.spaceR15')
        self.assertTrue(twitter.is_displayed(), 'Header twitter icon is not displayed')
        linkedin = self.driver.find_element_by_css_selector('.iconNav.navSocial.unit .fa.fa-linkedin.circle.spaceR15')
        self.assertTrue(linkedin.is_displayed(), 'Header linkedin icon is not displayed')
        pinterest = self.driver.find_element_by_css_selector('.iconNav.navSocial.unit .fa.fa-pinterest.circle.spaceR15')
        self.assertTrue(pinterest.is_displayed(), 'Header Pinterest icon is not displayed')
#        instagram = self.driver.find_element_by_css_selector('.navSocial .fa.fa-instagram.circle.spaceR15')
#        self.assertTrue(instagram.is_displayed(), "Header instagram icon is not displayed")
        
    def testSearch(self):
        browser_name = env_util.get_browser()
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(browser_name == "safari"):
            search_icon.click()
        else:
            webdriver_util.hover(self.driver, search_icon)
        time.sleep(5)
        search = self.driver.find_element_by_css_selector('.searchPanel')
        assert search.is_displayed() == True
        position = search.location
        y_pos = position.get('y')
        assert y_pos == 81.0
        
    def testSubNavigation(self):
        sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
#        nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.bg5')
        self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
        nav_links = self.driver.find_elements_by_css_selector('.altNavList.line.mqMedOff .subItem>a')
        for link in nav_links:
            self.assertTrue(link.is_displayed(), 'sub nav link is not displayed')
        sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
#        nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
        sub_nav_color = sub_nav.value_of_css_property('background-color')
        sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
        self.assertEquals(sub_nav_color,sub_nav_bar_color, 'nav bar color and color behind nav links do not match')
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            expected_color = u'rgba(23, 166, 255, 1)'
        else:
            expected_color = u'rgb(23, 166, 255)' 
        self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
        side_ads_css = '#ctMedia'
        if(webdriver_util.is_element_present(self.driver, side_ads_css)):
            if("chrome" or "headless" in browser_name):
                expected_color = u'rgba(0, 0, 0, 0)'
            else:
                expected_color = u'rgba(0, 0, 0)'
            self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')
#        else:
#            self.assertEqual(sub_nav_color, sub_nav_bar_color, 'Extended bar color is not correct')
        
    '''def testAdDisclaimer(self):
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
        self.assertEquals(learn_more_url, LEARN_MORE_URL, "actual [{0}] doesn't match expected [{1}]".format(learn_more_url, LEARN_MORE_URL))'''
        
    def testBreadCrumb(self):
        lv_one = self.driver.find_element_by_xpath("//div[@class='css-1lz4q4o efjv07h0']/a[1]").text.strip()
        lv_two = self.driver.find_element_by_xpath("//div[@class='css-1lz4q4o efjv07h0']/a[2]").text.strip()
        self.assertEquals(lv_one, ONE, "One {0} doesn't match the {1}".format(lv_one, ONE))
        self.assertEquals(lv_two, TWO, "Two {0} doesn't match the {1}".format(lv_two, TWO))
        lv_one_bc = self.driver.find_element_by_xpath("//div[@class='css-1lz4q4o efjv07h0']/a[1]")
        color = lv_one_bc.value_of_css_property("color")
        browser_name = env_util.get_browser()
        if("chrome" or "headless" in browser_name):
            self.assertEqual("rgba(255, 255, 255, 1)", color, "Bread crumbs color was changed")
        else:
            self.assertEqual("rgb(0, 126, 204)", color, "Bread crumbs color was changed")
    
    def testHeadline(self):
        headline = self.driver.find_element_by_css_selector('.css-5nia1y.elbhbli2')
        self.assertTrue(headline.is_displayed(), 'Article headline is not displayed')
        headline_text = headline.text.strip()
        if 'prod' in env_util.get_env():
            self.assertEquals(headline_text, PROD_HEADLINE, "actual [{0}] doesn't match expected [{1}]".format(headline_text, PROD_HEADLINE))
        else:
            self.assertEquals(headline_text, HEADLINE, "actual [{0}] doesn't match expected [{1}]".format(headline_text, HEADLINE))  
         
    def testByLine(self):
        env = env_util.get_env()
        author_date = self.driver.find_element_by_xpath("//*[@class='css-1flyc9m elbhbli3']")
        self.assertTrue(author_date.is_displayed(), 'Author & Date is not displayed')
        author_date_text = author_date.text
        author_date_text.encode('ascii','ignore')
        i = author_date_text.find("\n")
        author_name = author_date_text[:i]
        if 'prod' in env:
            self.assertEquals(author_name, PROD_AUTHOR, "actual [{0}] doesn't match expected [{1}]".format(author_name, PROD_AUTHOR))
        else:
            self.assertEquals(author_name, AUTHOR, "actual [{0}] doesn't match expected [{1}]".format(author_name, AUTHOR))
#        date = self.driver.find_element_by_xpath("//*[@class='css-1flyc9m elbhbli3']")
#        self.assertTrue(date.is_displayed(), "'Publish date is not displayed")
        date_text = author_date_text[i+1:]
        if 'prod' in env:
            self.assertEquals(date_text, PROD_PUBLISH_DATE, "actual [{0}] doesn't match expected [{1}]".format(date_text, PROD_PUBLISH_DATE))
        else:
            self.assertEquals(date_text, PUBLISH_DATE, "actual [{0}] doesn't match expected [{1}]".format(date_text, PUBLISH_DATE))

        fb = self.driver.find_element_by_xpath("//div[@class='css-m37a3p e48afky0']/div[2]")
        self.assertTrue(fb.is_displayed(), 'Facebook social share icon is displayed')
        twitter = self.driver.find_element_by_xpath("//div[@class='css-m37a3p e48afky0']/div[3]")
        self.assertTrue(twitter.is_displayed(), 'Twitter social share icon is displayed')
        linkedin = self.driver.find_element_by_xpath("//div[@class='css-m37a3p e48afky0']/div[1]")
        self.assertTrue(linkedin.is_displayed(), 'Linkedin social share icon is displayed')
        google = self.driver.find_element_by_xpath("//div[@class='css-m37a3p e48afky0']/div[4]")
        self.assertTrue(google.is_displayed(), 'Google+ social share icon is displayed')
               
    def testContent(self):
        first_header_text = self.driver.find_element_by_css_selector('.css-1wc1ys3.e7scxr02').text
        self.assertEquals(first_header_text,FIRST_HEADER, 'Header text is incorrect')
        first_header_details = self.driver.find_element_by_css_selector('.css-1s806mh.e7scxr01')
        self.assertTrue(first_header_details.is_displayed(), 'No details shown in "Our Best Picks" section')
        full_list = self.driver.find_element_by_css_selector('.css-f95ul7.e1mccs7b4')
        try:
            full_list.click()
        except WebDriverException:
            print 'Element is not clickable'
        best_picks = self.driver.find_element_by_css_selector('.css-whh993.e1mccs7b4')
        try:
            best_picks.click()
        except WebDriverException:
            print 'Element is not clickable'
        fulllist_text = self.driver.find_element_by_css_selector('.css-1wc1ys3.emoppjr2').text
        self.assertEquals(fulllist_text,FULLLIST_HEADER, 'Full List Header text is not matched')
        
        full_list_content = self.driver.find_element_by_css_selector('.css-pi1ck8.e1ilq5g20')
        best_picks_content = self.driver.find_element_by_css_selector('.css-pi1ck8.e1ilq5g20')
        best_pick_badge = self.driver.find_element_by_css_selector('.css-d10k5o.e1ilq5g21')
        if full_list.click():
            self.assertTrue(full_list_content.is_displayed(), "No content in full list section")
        if best_picks.click():
            self.assertTrue(best_picks_content.is_displayed(), "No content in best picks section")
            self.assertTrue(best_pick_badge.is_displayed(), "No badge icon in best picks section")
        
        author_bio = self.driver.find_element_by_css_selector('.css-bamw51.ey98x0n0')
        self.assertTrue(author_bio.is_displayed(), "Author bio section is not displayed")
        author_image = self.driver.find_element_by_css_selector('.css-1xqaf2r.ey98x0n1')
        self.assertTrue(author_image.is_displayed(), "Author image is not displayed")
        author_name = self.driver.find_element_by_css_selector('.css-1up8trb.ey98x0n3')
        self.assertTrue(author_name.is_displayed(), "Author name is not displayed")
        author_blurb = self.driver.find_element_by_css_selector('.css-1kx6sb5.ey98x0n4')
        self.assertTrue(author_blurb.is_displayed(), "Author blurb is not displayed")
        author_twitter = self.driver.find_element_by_css_selector('.css-1l95nvm.ey98x0n5 .fa.fa-twitter.circle.spaceR15')
        self.assertTrue(author_twitter.is_displayed(), "Author twitter is not displayed")
        
    def testWidget(self):
        widgets = self.driver.find_elements_by_css_selector('.bz__RfqWidget')
        self.assertTrue(len(widgets) == 2, '[Current: '+str(len(widgets))+' widgets] [Expected: 2 widgets]')
        for widget in widgets:
            self.assertTrue(widget.is_displayed(), 'Widget is not displayed')
            question = self.driver.find_element_by_css_selector('.bz__Question')
            self.assertTrue(question.is_displayed(), 'Question is not displayed')
            answer = self.driver.find_element_by_css_selector('.bz__AnswerLabel')
            self.assertTrue(answer.is_displayed(), 'Answer is not displayed')
            #next_button = self.driver.find_element_by_css_selector('#btnNext')
            #self.assertTrue(next_button.is_displayed(), 'Next Button is not displayed')
        
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
#        print "New", all_url
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
    suite = unittest.TestLoader().loadTestsFromTestCase(OptimizedTemplateTestCase)
    unittest.TextTestRunner().run(suite) 
        
        