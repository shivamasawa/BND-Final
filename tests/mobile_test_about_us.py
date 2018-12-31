#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import time
import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util

WEB_SITE = env_util.get_env_url()
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]
COMPANY_LINKS = ['Company Info', 'About Us','Contact Us','Advertise with Us','Using Our Content','Licensing & Reprints','Copyright Policy','Terms of Use','Privacy Policy','Sitemap']
COMPANY_URLS = ['http://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/', WEB_SITE+'sitemap']
COMPANY_URLS_MOBILE = ['https://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/',WEB_SITE+'sitemap']
COMPANY_URLS_TABLET = ['http://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/',WEB_SITE+'sitemap']
NETWORK_LINKS = ["Top Ten Reviews","Tom's Guide","Laptop Mag","Tom's Hardware","Business News Daily","Tom's IT Pro","Space.com","Live Science","Anand Tech","Active Junky","ShopSavvy"]
NETWORK_URLS = ['http://www.toptenreviews.com/','https://www.tomsguide.com/','https://www.laptopmag.com/','https://www.tomshardware.com/','https://www.businessnewsdaily.com/','http://www.tomsitpro.com/','https://www.space.com/','https://www.livescience.com/','https://www.anandtech.com/','https://activejunky.com/','https://shopsavvy.com/']
COPYRIGHT = u'Copyright © '+str(datetime.datetime.now().year)+u' All Rights Reserved.'

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    width = web_element.size.get('width')
    assert (width <= browser_width) and (width >= (browser_width - 50))

class AboutUsTestCase(mobile_test_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(AboutUsTestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
        try:
            driver.get(WEB_SITE+'about')
        except Exception as e:
            driver.quit()
            raise e
        
    def testHeader(self):
        header = self.driver.find_element_by_css_selector('.masthead.cf')
        self.assertTrue(header.is_displayed(), 'Header is not displayed')
        if 'phone' in self.device_name:
            color_bar = self.driver.find_element_by_css_selector('.sectRule.allColors.spaceB10.mqMedOn')
            verifyElementIsDisplayedAndSpansWidth(self, color_bar)
            logo = self.driver.find_element_by_css_selector('div.logo a>img.mqMedOn')
            self.assertTrue(logo.is_displayed(), 'Logo is not displayed')
            menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
            self.assertTrue(menu_icon.is_displayed(), 'Menu icon is not displayed')
            menu_panel = self.driver.find_element_by_css_selector('.menuPanel')
            self.assertFalse(menu_panel.is_displayed(), 'menu panel is displayed')
            menu_icon.click()
            time.sleep(1)
            verifyElementIsDisplayedAndSpansWidth(self, menu_panel)
            menu_icon.click()
            time.sleep(1)
            self.assertFalse(menu_panel.is_displayed(), 'menu panel is displayed')
        else:
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
            instagram = self.driver.find_element_by_css_selector('.navSocial .fa.fa-instagram.circle.spaceR15')
            self.assertTrue(instagram.is_displayed(), "Header instagram icon is not displayed")
    
    def testSearch(self):
        search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
        if(self.device_name.__contains__('ipad') or self.device_name.__contains__('tablet')):
            if(self.device_name.__contains__('ipad')):
                mobile_util.tap_webview_element_with_offset(self.driver, self.device_name, search_icon, 20)
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
        self.assertEqual(len(corporate_links), 4, "4 corporate links are not displayed")
        for link in corporate_links:
            self.assertTrue(link.is_displayed(), "One of the corporate links is not displayed")
        
    def testMoreResourcesLinks(self):
        more_resources_heading = self.driver.find_element_by_xpath("//aside/div[@class='mod'][2]/h2")
        self.assertTrue(more_resources_heading.is_displayed(), 'Corporate heading is not displayed')
        resources_links = self.driver.find_elements_by_xpath("//aside/div[@class='mod'][2]/ul/li/a")
        self.assertEqual(len(resources_links), 11, "11 corporate links are not displayed")
        for link in resources_links:
            self.assertTrue(link.is_displayed(), "One of the corporate links is not displayed")
        
    def testFooter(self):
        sub_menus = self.driver.find_elements_by_css_selector(".unit.netLinks")
        if 'phone' in self.device_name:
            for sub_group in sub_menus:
                self.assertFalse(sub_group.is_displayed(), 'link group in footer is displayed')        
        else:
            all_url = []
            for sub_group in sub_menus:
                self.assertTrue(sub_group.is_displayed(), 'link group in footer is not displayed')
                column = []
                url_category = sub_group.find_element_by_tag_name("a").get_attribute("href")
                column.append(url_category)
                list_of_li = sub_group.find_elements_by_css_selector(".netLink")
                for i in list_of_li:
                    #line_url = i.get_attribute("href")
                    line_text = i.text
                    #column.append(line_url)
                    column.append(line_text)
                all_url.append(column)
            print "New", all_url
            print "Old", FOOTER
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
        self.assertEquals(copyright_text, COPYRIGHT, "Copyright message is not correct")
        company = self.driver.find_element_by_xpath('html/body/footer/div[1]/div/section[1]/header')
        company_text = company.text
        if 'phone' in self.device_name:
            self.assertFalse(company.is_displayed(), 'Company heading is displayed in footer on mobile devices')
            company_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/div[1]/div/a')
        else:
            self.assertEquals(company_text, "COMPANY", "actual [{0}] doesn't match expected [{1}]".format(company_text, "COMPANY"))
            company_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/section[1]/ul/li/a')
        for i in range(0, len(company_links)):
            link = company_links[i]
            link_text = link.text
            self.assertEquals(link_text, COMPANY_LINKS[i], "actual [{0}] doesn't match expected [{1}]".format(link_text, COMPANY_LINKS[i]))
            link_url = link.get_attribute('href')
            if 'phone' in self.device_name:
                self.assertEquals(link_url, COMPANY_URLS_MOBILE[i], "actual [{0}] doesn't match expected [{1}]".format(link_url, COMPANY_URLS_MOBILE[i]))
            else:
                self.assertEquals(link_url, COMPANY_URLS_TABLET[i], "actual [{0}] doesn't match expected [{1}]".format(link_url, COMPANY_URLS_TABLET[i]))

        network = self.driver.find_element_by_xpath('html/body/footer/div[1]/div/section[2]/header')
        network_text = network.text
        network_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/section[2]/ul/li/a')
        if 'phone' in self.device_name:
            self.assertFalse(network.is_displayed(), "Network heading is displayed in footer on mobile devices")
            for link in network_links:
                self.assertFalse(link.is_displayed(), "One or more network links displayed on mobile device")
        else:
            self.assertEquals(network_text, "NETWORK", "actual [{0}] doesn't match expected [{1}]".format(network_text, "NETWORK"))
            for i in range(0, len(company_links)):
                link = network_links[i]
                link_text = link.text
                self.assertEquals(link_text, NETWORK_LINKS[i], "actual [{0}] doesn't match expected [{1}]".format(link_text, NETWORK_LINKS[i]))
                link_url = link.get_attribute('href')
                self.assertEquals(link_url, NETWORK_URLS[i], "actual [{0}] doesn't match expected [{1}]".format(link_url, NETWORK_URLS[i]))
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AboutUsTestCase)
    unittest.TextTestRunner().run(suite) 