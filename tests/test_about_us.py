#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import time
import datetime
import sys
import os
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.common.by import By
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util, webdriver_util
#env_util.envor = ''
WEB_SITE = env_util.get_env_url()
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]
COMPANY_LINKS = ['About Us','Contact Us','Partner with Us','Copyright Policy','Terms of Use','Privacy Policy','Advertising Disclosure','Sitemap']
COMPANY_URLS = [WEB_SITE+'about','mailto:%20editor@business.com','https://www.business.com/partner/#overview',WEB_SITE+'copyright-policy',WEB_SITE+'terms-of-use',WEB_SITE+'privacy-policy',WEB_SITE+'advertising-disclosure',WEB_SITE+'sitemap']
NETWORK_LINKS = ["Business.com", "BuyerZone.com"]
NETWORK_URLS = ['https://www.business.com/','https://www.buyerzone.com/']
COPYRIGHT = u'Copyright © '+str(datetime.datetime.now().year)+u' All Rights Reserved.'

class AboutUsTestCase(test_core.TestCore):
    
    @classmethod
    def setUpClass(cls):
        super(AboutUsTestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        try:
            driver.get(WEB_SITE+'about')
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
        #element = WebDriverWait(self.driver,5).until(EC.presence_of_element_located(By.CLASS_NAME, 'searchPanel'),"Error")
        assert search.is_displayed() == True
        position = search.location
        y_pos = position.get('y')
        assert y_pos == 81.0
    
    def testContent(self):
        heading = self.driver.find_element_by_css_selector('section h1')
        self.assertTrue(heading.is_displayed(), 'About us heading is not displayed')
        about_content = self.driver.find_element_by_css_selector('section h1+p')
        self.assertTrue(about_content.is_displayed(), "About us paragraph is not displayed")
        mission_heading = self.driver.find_element_by_xpath('//section[1]/h2[1]')
        self.assertTrue(mission_heading.is_displayed(), 'Mission Statement heading is not displayed')
        mission_statement = self.driver.find_element_by_xpath('//section[1]/h2[1]/following-sibling::p')
        self.assertTrue(mission_statement.is_displayed(), 'Mission statement is not displayed')
        history_heading = self.driver.find_element_by_xpath('//section[1]/h2[2]')
        self.assertTrue(history_heading.is_displayed(), 'Our History heading is not displayed')
        our_history = self.driver.find_element_by_xpath('//section[1]/h2[2]/following-sibling::p')
        self.assertTrue(our_history.is_displayed(), 'Our History section is not displayed')
        
    def testOurPeople(self):
        our_people_heading = self.driver.find_element_by_xpath('//section[2]/h2')
        self.assertTrue(our_people_heading.is_displayed(), 'Our People heading is not displayed')
        about_items = self.driver.find_elements_by_css_selector('div.aboutItem')
        i=1
        for item in about_items:
            image = item.find_element_by_css_selector('a>img')
            self.assertTrue(image.is_displayed(), 'Image not displayed for person '+str(i))
            heading = item.find_element_by_css_selector('h3')
            self.assertTrue(heading.is_displayed(), 'Name/title not displayed for person '+str(i))
            email = item.find_element_by_css_selector('div>a.mailTo')
            self.assertTrue(email.is_displayed(), 'Email not displayed for person '+str(i))
            social = item.find_element_by_css_selector('div.iconNav')
            self.assertTrue(social.is_displayed(), 'Social icon section not displayed for person '+str(i))
            description = item.find_element_by_tag_name('p')
            self.assertTrue(description.is_displayed(), 'Description not displayed for person '+str(i))
            i=i+1
        
    def testLocationAndContact(self):
        location_heading = self.driver.find_element_by_css_selector('div.mod.topMod > h2')
        self.assertTrue(location_heading.is_displayed(), 'Location heading is not displayed')
        address_content = self.driver.find_element_by_css_selector('address.aboutAddress')
        self.assertTrue(address_content.is_displayed(), 'Address is not displayed')
    
    def testCorporateLinks(self):
        corporate_heading = self.driver.find_element_by_xpath("//aside/div[@class='mod'][1]/h2")
        self.assertTrue(corporate_heading.is_displayed(), 'Corporate heading is not displayed')
        corporate_links = self.driver.find_elements_by_xpath("//aside/div[@class='mod'][1]/ul/li/a")
        self.assertEqual(len(corporate_links), 2, "2 corporate links are not displayed")
        for link in corporate_links:
            self.assertTrue(link.is_displayed(), "One of the corporate links is not displayed")
        
    def testMoreResourcesLinks(self):
        more_resources_heading = self.driver.find_element_by_xpath("//aside/div[@class='mod'][2]/h2")
        self.assertTrue(more_resources_heading.is_displayed(), 'Corporate heading is not displayed')
        resources_links = self.driver.find_elements_by_xpath("//aside/div[@class='mod'][2]/ul/li/a")
        self.assertEqual(len(resources_links), 10, "10 corporate links are not displayed")
        for link in resources_links:
            self.assertTrue(link.is_displayed(), "One of the corporate links is not displayed")
        
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
        #print ("New", all_url)
        #print ("Expected", FOOTER)
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
    suite = unittest.TestLoader().loadTestsFromTestCase(AboutUsTestCase)
    unittest.TextTestRunner().run(suite) 