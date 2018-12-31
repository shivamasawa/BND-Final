#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import random
import time
import test_mobile_core
import mobile_util
import webdriver_util
import datetime

WEB_SITE = "https://www.businessnewsdaily.com/"
ARTICLES = ["2389-jobs-travel-lovers.html","2747-great-business-ideas.html","1646-great-business-ideas-2012.html","1999-great-business-ideas-2012.html","5126-best-jobs-introverts.html"]



DISCLAIMER_TEXT = u'Product and service reviews are conducted independently by our editorial team, but we sometimes make money when you click on links. Learn more.'
LEARN_MORE_URL = 'https://purch.com/advertising-disclosure/'
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]
COMPANY_LINKS = ['Company Info', 'About Us','Contact Us','Advertise with Us','Using Our Content','Licensing & Reprints','Copyright Policy','Terms of Use','Privacy Policy','Sitemap']
COMPANY_URLS = ['http://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/', WEB_SITE+'sitemap']
COMPANY_URLS_MOBILE = ['https://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/',WEB_SITE+'sitemap']
COMPANY_URLS_TABLET = ['http://purch.com/',WEB_SITE+'about','http://purch.com/about/#contact','http://purch.com/advertise/','http://purch.com/#contact','http://purch.com/#contact','http://purch.com/copyright-policy/','http://purch.com/terms-of-use/','http://purch.com/privacy-policy/',WEB_SITE+'sitemap']
NETWORK_LINKS = ["Top Ten Reviews","Tom's Guide","Laptop Mag","Tom's Hardware","Business News Daily","Tom's IT Pro","Space.com","Live Science","Anand Tech","Active Junky","ShopSavvy"]
NETWORK_URLS = ['http://www.toptenreviews.com/','https://www.tomsguide.com/','https://www.laptopmag.com/','https://www.tomshardware.com/','https://www.businessnewsdaily.com/','http://www.tomsitpro.com/','https://www.space.com/','https://www.livescience.com/','https://www.anandtech.com/','https://activejunky.com/','https://shopsavvy.com/']
COPYRIGHT = u'Copyright © '+str(datetime.datetime.now().year)+u' All Rights Reserved.'

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    platform_name = mobile_util.get_platform_name(self.driver);
    browser_width = mobile_util.get_browser_width(platform_name, self.driver)
    width = web_element.size.get('width')
    assert (width <= browser_width) and (width >= (browser_width - 50))

class CountdownTestCase(test_mobile_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(CountdownTestCase, cls).setUpClass()
        driver = test_mobile_core.MobileTestCore.driver
        try:
            url = WEB_SITE+ARTICLES[random.randint(0, len(ARTICLES)-1)]
            driver.get(url)
        except Exception as e:
            driver.quit()
            raise e
        
    
    def testCountdown(self):  
        print("================ Countdown Page Test ================")
        errors = []  
        #testHeader
        try:
            header = self.driver.find_element_by_css_selector('.masthead.cf')
            self.assertTrue(header.is_displayed(), 'Header is not displayed')
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
            print("testHeader: pass")
        except Exception as err:
            print("testHeader: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testSearch
        try:
            search_icon = self.driver.find_element_by_css_selector('.searchIcon.fa.fa-search.circle.circleAlt')
            self.driver.execute_script('window.scrollTo(0,0)')
            menu_icon = self.driver.find_element_by_css_selector('.menuIcon')
            menu_icon.click()
            time.sleep(1)
            self.driver.execute_script('window.scrollTo(0,0)')
            search = self.driver.find_element_by_css_selector('.searchPanel')
            assert search.is_displayed() == True
            position = search.location
            y_pos = position.get('y')
            assert y_pos == 54.0
            menu_icon.click()
            print("testSearch: pass")
        except Exception as err:
            print("testSearch: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testAdDisclaimer
        try:
            disclaimer = self.driver.find_element_by_css_selector('.FTCdisclosure')
            actual_text = disclaimer.text.strip()
            self.assertEquals(actual_text, DISCLAIMER_TEXT, "actual [{0}] doesn't match expected [{1}]".format(actual_text, DISCLAIMER_TEXT))
            learn_more = self.driver.find_element_by_css_selector('.FTCdisclosure>a')
            actual_text = learn_more.text.strip()
            expected_text = "Learn more."
            self.assertEquals(actual_text, expected_text, "actual [{0}] doesn't match expected [{1}]".format(actual_text, expected_text))
            learn_more_url = learn_more.get_attribute('href')
            self.assertEquals(learn_more_url, LEARN_MORE_URL, "actual [{0}] doesn't match expected [{1}]".format(learn_more_url, LEARN_MORE_URL))
            print("testAdDisclaimer: pass")
        except Exception as err:
            print("testAdDisclaimer: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testBreadCrumb
        try:
            lv_one = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:first-child")
            self.assertTrue(lv_one.is_displayed(), "First breadcrumb not displayed");
            lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child")
            self.assertTrue(lv_two.is_displayed(), "Second breadcrumb is not displayed")
            lv_two_bc = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child>a")
            color = lv_two_bc.value_of_css_property("color")
            self.assertEqual("rgba(0, 126, 204, 1)", color, "Bread crumbs color was changed")
            print("testBreadCrumb: pass")
        except Exception as err:
            print("testHeader: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testHeadline
        try:
            headline = self.driver.find_element_by_css_selector('.h1.nolinks')
            self.assertTrue(headline.is_displayed(), 'Article headline is not displayed')
            print("testHeadline: pass")
        except Exception as err:
            print("testHeadline: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testByLine
        try:
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
            print("testByLine: pass")
        except Exception as err:
            print("testByLine: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testContent
        try:
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
                    try:
                        right_arrow.click()
                    except:
                        webdriver_util.scroll_to_element(self.driver, right_arrow)
                        right_arrow.click()
            print("testContent: pass")
        except Exception as err:
            print("testContent: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testAuthor
        try:
            author_name = self.driver.find_element_by_css_selector('.authorName')
            self.assertTrue(author_name.is_displayed(), "Author name not displayed")
            author_about = self.driver.find_element_by_css_selector('.authorDesc>p')
            self.assertTrue(author_about.is_displayed(), "Author about not displayed")
            author_image = self.driver.find_element_by_css_selector('img.author-thumb')
            self.assertTrue(author_image.is_displayed(), "Author image not displayed")
            author_twitter = self.driver.find_element_by_css_selector('.socialByline>a')
            self.assertTrue(author_twitter, "Author twitter not displayed")
            print("testAuthor: pass")
        except Exception as err:
            print("testAuthor: FAIL")
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testRelatedSection
        try:
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
            print("testRelatedSection: pass")
        except Exception as err:
            print("testRelatedSection: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testFooter
        try:
            sub_menus = self.driver.find_elements_by_css_selector(".unit.netLinks")
            for sub_group in sub_menus:
                self.assertFalse(sub_group.is_displayed(), 'link group in footer is displayed')        
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
            self.assertFalse(company.is_displayed(), 'Company heading is displayed in footer on mobile devices')
            company_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/div[1]/div/a')
            for i in range(0, len(company_links)):
                link = company_links[i]
                link_text = link.text
                self.assertEquals(link_text, COMPANY_LINKS[i], "actual [{0}] doesn't match expected [{1}]".format(link_text, COMPANY_LINKS[i]))
                link_url = link.get_attribute('href')
                self.assertEquals(link_url, COMPANY_URLS_MOBILE[i], "actual [{0}] doesn't match expected [{1}]".format(link_url, COMPANY_URLS_MOBILE[i]))
            network = self.driver.find_element_by_xpath('html/body/footer/div[1]/div/section[2]/header')
            network_text = network.text
            network_links = self.driver.find_elements_by_xpath('html/body/footer/div[1]/div/section[2]/ul/li/a')
            self.assertFalse(network.is_displayed(), "Network heading is displayed in footer on mobile devices")
            for link in network_links:
                self.assertFalse(link.is_displayed(), "One or more network links displayed on mobile device")
            print("testFooter: pass")
        except Exception as err:
            print("testFooter: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        print("URL Tested: "+self.driver.current_url)
        if(len(errors) > 0):
            print("Total Failures/Errors: "+str(len(errors)))
            print("===================================================")
            raise errors[0]
    
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CountdownTestCase)
    unittest.TextTestRunner().run(suite) 
        
        