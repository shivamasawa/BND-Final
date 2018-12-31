#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import datetime
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util, webdriver_util

WEB_SITE = env_util.get_env_url()
SITE = WEB_SITE+'7839-best-crm-software.html'
DISCLAIMER_TEXT = 'Product and service reviews are conducted independently by our editorial team, but we sometimes make money when you click on links. Learn more.'
LEARN_MORE_URL = 'https://purch.com/advertising-disclosure/'
ONE = 'Find a Solution'
TWO = 'Marketing Solutions'
HEADLINE = 'Best CRM Software 2018'
PROD_HEADLINE = 'Best CRM Software 2018'
AUTHOR = 'Mona Bushnell, B2B Tech Writer'
PROD_AUTHOR = 'Mona Bushnell, B2B Tech Writer'
PUBLISH_DATE = 'April 27, 2018 01:45 pm EST'
PROD_PUBLISH_DATE = 'April 27, 2018 01:45 pm EST'
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]
COMPANY_LINKS = ['Company Info', 'About Us','Contact Us','Advertise with Us','Using Our Content','Licensing & Reprints','Copyright Policy','Terms of Use','Privacy Policy','Sitemap']
COMPANY_URLS_MOBILE = ['https://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/',WEB_SITE+'sitemap']
COMPANY_URLS_TABLET = ['http://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/',WEB_SITE+'sitemap']
NETWORK_LINKS = ["Top Ten Reviews","Tom's Guide","Laptop Mag","Tom's Hardware","Business News Daily","Tom's IT Pro","Space.com","Live Science","Anand Tech","Active Junky","ShopSavvy"]
NETWORK_URLS = ['http://www.toptenreviews.com/','https://www.tomsguide.com/','https://www.laptopmag.com/','https://www.tomshardware.com/','https://www.businessnewsdaily.com/','http://www.tomsitpro.com/','https://www.space.com/','https://www.livescience.com/','https://www.anandtech.com/','https://activejunky.com/','https://shopsavvy.com/']
COPYRIGHT = u'Copyright © '+str(datetime.datetime.now().year)+u' All Rights Reserved.'

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    width = web_element.size.get('width')
    assert (width <= browser_width) and (width >= (browser_width - 50))

class OptimizedTemplateTestCase(mobile_test_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(OptimizedTemplateTestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
        try:
            driver.get(SITE)
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
        
    def testSubNavigation(self):
        sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
        if not ('phone' in self.device_name):
            self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
            sub_nav_bar = self.driver.find_element_by_css_selector('.altNav.unit')
            nav_link_bar_part = self.driver.find_element_by_css_selector('.altNavList.line.bg5')
            self.assertTrue(sub_nav_bar.is_displayed(), 'sub navigation bar is not displayed')
            nav_links = self.driver.find_elements_by_css_selector('.altNavList.line.bg5 .subItem>a')
            for link in nav_links:
                self.assertTrue(link.is_displayed(), 'sub nav link is not displayed')
            sub_nav = self.driver.find_element_by_css_selector('.wrap.altNavLiner')
            nav_link_color = nav_link_bar_part.value_of_css_property('background-color')
            sub_nav_color = sub_nav.value_of_css_property('background-color')
            sub_nav_bar_color = sub_nav_bar.value_of_css_property('background-color')
            self.assertEquals(nav_link_color, sub_nav_color, 'nav bar color and color behind nav links do not match')
            expected_color = u'rgba(23, 166, 255, 1)'
            self.assertEqual(sub_nav_color, expected_color, 'color is not correct')
            side_ads_css = '#ctMedia'
            if(webdriver_util.is_element_present(self.driver, side_ads_css)):
                expected_color = u'rgba(0, 0, 0, 0)'
                self.assertEquals(sub_nav_bar_color, expected_color, ' Nav bar is covering background/side ads')
            else:
                self.assertEqual(sub_nav_color, sub_nav_bar_color, 'Extended bar color is not correct')
        
    def testAdDisclaimer(self):
        disclaimer = self.driver.find_element_by_css_selector('.FTCdisclosure')
        actual_text = disclaimer.text
        self.assertEquals(actual_text, DISCLAIMER_TEXT, "actual [{0}] doesn't match expected [{1}]".format(actual_text, DISCLAIMER_TEXT))
        learn_more = self.driver.find_element_by_css_selector('.FTCdisclosure>a')
        actual_text = learn_more.text
        expected_text = "Learn more."
        self.assertEquals(actual_text, expected_text, "actual [{0}] doesn't match expected [{1}]".format(actual_text, expected_text))
        learn_more_url = learn_more.get_attribute('href')
        self.assertEquals(learn_more_url, LEARN_MORE_URL, "actual [{0}] doesn't match expected [{1}]".format(learn_more_url, LEARN_MORE_URL))
        
    def testBreadCrumb(self):
        lv_one = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:first-child").text
        lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child").text
        self.assertEquals(lv_one, ONE, "One {0} doesn't match the {1}".format(lv_one, ONE))
        self.assertEquals(lv_two, TWO, "Two {0} doesn't match the {1}".format(lv_two, TWO))
        lv_two_bc = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child>a")
        color = lv_two_bc.value_of_css_property("color")
        self.assertEqual("rgba(0, 126, 204, 1)", color, "Bread crumbs color was changed")
    
    def testHeadline(self):
        headline = self.driver.find_element_by_css_selector('.h1.nolinks')
        self.assertTrue(headline.is_displayed(), 'Article headline is not displayed')
        headline_text = headline.text
        if 'prod' in env_util.get_env():
            self.assertEquals(headline_text, PROD_HEADLINE, "actual [{0}] doesn't match expected [{1}]".format(headline_text, PROD_HEADLINE))
        else:
            self.assertEquals(headline_text, HEADLINE, "actual [{0}] doesn't match expected [{1}]".format(headline_text, HEADLINE))
        
    def testByLine(self):
        env = env_util.get_env()
        author = self.driver.find_element_by_css_selector('.author')
        self.assertTrue(author.is_displayed(), 'Author is not displayed')
        author_text = author.text
        if 'prod' in env:
            self.assertEquals(author_text, PROD_AUTHOR, "actual [{0}] doesn't match expected [{1}]".format(author_text, PROD_AUTHOR))
        else:
            self.assertEquals(author_text, AUTHOR, "actual [{0}] doesn't match expected [{1}]".format(author_text, AUTHOR))
        date = self.driver.find_element_by_css_selector('.byline>time')
        self.assertTrue(date.is_displayed(), "'Publish date is not displayed")
        date_text = date.text.strip()
        if 'prod' in env:
            self.assertEquals(date_text, PROD_PUBLISH_DATE, "actual [{0}] doesn't match expected [{1}]".format(date_text, PROD_PUBLISH_DATE))
        else:
            self.assertEquals(date_text, PUBLISH_DATE, "actual [{0}] doesn't match expected [{1}]".format(date_text, PUBLISH_DATE))
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
        content = self.driver.find_element_by_css_selector('.article.unitExt.col2.article-text.wide-article')
        content_width = content.size.get('width')
        if 'phone' in self.device_name:
            content_width = content.size.get('width')
        else:
            self.assertEqual(content_width, 1000, 'Content width is not 1000')
        image = self.driver.find_element_by_css_selector('.magnify-wrapper img')
        if 'phone' in self.device_name:
            verifyElementIsDisplayedAndSpansWidth(self, image)
        else:
            img_width = image.size.get('width')
            img_height = image.size.get('height')
            self.assertEquals(img_width, 300, "actual width [{0}] doesn't match expected [{1}]".format(img_width, 300))
            self.assertEquals(img_height, 200, "actual height [{0}] doesn't match expected [{1}]".format(img_height, 200))
        comparison = self.driver.find_element_by_css_selector('.sc-chart')
        self.assertTrue(comparison.is_displayed(), "Comparison section is not displayed")
        comparison_width = comparison.size.get('width')
        self.assertTrue(comparison_width <= content_width and comparison_width >= content_width-50, "comparison section does not span width of content")
        info_cards = self.driver.find_elements_by_css_selector('.info-card')
        for card in info_cards:
            self.assertTrue(card.is_displayed(), 'info card is not displayed')
            image = card.find_element_by_css_selector('.info-card_img')
            self.assertTrue(image.is_displayed(), 'Product logo not displayed')
            name = card.find_element_by_css_selector('.info-card_biz-name.u-x-spacing')
            self.assertTrue(name.is_displayed(), 'product name is not displayed')
            review_button = card.find_element_by_css_selector('.info-card_review-btn')
            self.assertTrue(review_button.is_displayed(), 'review button is not displayed')
            details = card.find_element_by_css_selector('.info-card>ul')
            self.assertTrue(details.is_displayed(), 'product details are not displayed')
            if 'phone' in self.device_name:
                verifyElementIsDisplayedAndSpansWidth(self, card)
        author_bio = self.driver.find_element_by_css_selector('.line.authorBio')
        self.assertTrue(author_bio.is_displayed(), "Author bio section is not displayed")
        author_image = self.driver.find_element_by_css_selector('.author-thumb')
        self.assertTrue(author_image.is_displayed(), "Author image is not displayed")
        author_name = self.driver.find_element_by_css_selector('.authorName')
        self.assertTrue(author_name.is_displayed(), "Author name is not displayed")
        author_blurb = self.driver.find_element_by_css_selector('.authorDesc>p')
        self.assertTrue(author_blurb.is_displayed(), "Author blurb is not displayed")
        author_twitter = self.driver.find_element_by_css_selector('.authorBio .fa.fa-twitter.circle.spaceR15')
        self.assertTrue(author_twitter.is_displayed(), "Author twitter is not displayed")
        
    def testWidget(self):
        print(self.driver.current_url)
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
    suite = unittest.TestLoader().loadTestsFromTestCase(OptimizedTemplateTestCase)
    unittest.TextTestRunner().run(suite) 
        
        