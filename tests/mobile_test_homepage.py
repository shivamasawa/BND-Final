#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util

WEB_SITE = env_util.get_env_url()
BEST_PICKS = u'OUR BEST PICKS'
SUB_MENUS = [u'START YOUR BUSINESS', u'GROW YOUR BUSINESS', u'BUILD YOUR CAREER', u'LEAD YOUR TEAM', u'FIND A SOLUTION']
LATEST = WEB_SITE + "latest"
HUGE_IMG = "https://img.purch.com/rc/600x400/"
SMALL_IMG = "https://img.purch.com/rc/400x267/"
SEEMORE = {"START YOUR BUSINESS":WEB_SITE + "start-your-business",
           "GROW YOUR BUSINESS":WEB_SITE + "grow-your-business",
           "BUILD YOUR CAREER":WEB_SITE + "build-your-career",
           "LEAD YOUR TEAM":WEB_SITE + "lead-your-team",
           "FIND A SOLUTION":WEB_SITE + "find-a-solution"
           }
FOOTER = [[u''+ WEB_SITE + 'start-your-business', u'Business Ideas', u'Business Plans', u'Startup Basics', u'Startup Funding', u'Franchising', u'Success Stories', u'Entrepreneurs'], [u''+ WEB_SITE + 'grow-your-business', u'Sales & Marketing', u'Finances', u'Your Team', u'Technology', u'Social Media', u'Security'], [u''+ WEB_SITE + 'build-your-career', u'Get the Job', u'Get Ahead', u'Office Life', u'Work-Life Balance', u'Home Office'], [u''+ WEB_SITE + 'lead-your-team', u'Leadership', u'Women in Business', u'Managing', u'Strategy', u'Personal Growth'], [u''+ WEB_SITE + 'find-a-solution', u'HR Solutions', u'Financial Solutions', u'Marketing Solutions', u'Security Solutions', u'Retail Solutions', u'SMB Solutions']]

class HomepageTestCase(mobile_test_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(HomepageTestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
        try:
            driver.get(WEB_SITE)
        except Exception as e:
            driver.quit()
            raise e
     
    def testElementsVerification(self):
                
        #OUR BEST PICKS left rail
        best_picks = self.driver.find_element_by_css_selector(".sideHdr").text
        self.assertEqual(best_picks, BEST_PICKS, "Can't locate or verify the left rail")
        
        sub_list = []
        sub_menus = self.driver.find_elements_by_class_name("modTitle")
        for i in sub_menus:
            sub_list.append(i.text)
        self.assertEqual(sub_list, SUB_MENUS, "Can't find 5 elements on the page")
        
        #Check the presents of the latest url 
        te = self.driver.find_element_by_css_selector(".hpFeatures.mod.topMod .hpLatestHeadlines").get_attribute("href")
        #"http://www.businessnewsdaily.com/latest"
        self.assertEqual(te, LATEST, "Can't locate url to the latest news")
        
    def testImageSizeHuge(self):    
        link = self.driver.find_element_by_css_selector(".hpLeadImg a")
        image = self.driver.find_element_by_css_selector(".hpLeadImg img")
        src = image.get_attribute("src")
        src.encode('ascii','ignore')
        #print src
        self.assertTrue(HUGE_IMG in src, "Image src (with size) does not match expected. Check image size")
        #title = link.get_attribute("title")
        #image_alt = image.get_attribute("alt")
        #self.assertNotEqual(title, image_alt, "Link title and image alt are the same")
        
        
    def testImageSizeSmall(self):  
        link = self.driver.find_element_by_css_selector(".newsItems a")
        image = self.driver.find_element_by_css_selector(".newsItems img")
        src = image.get_attribute("src")
        src.encode('ascii','ignore')
        #print src
        self.assertTrue(SMALL_IMG in src, "Image src (with size) does not match expected. Check image size")
        title = link.get_attribute("title")
        image_alt = image.get_attribute("alt")
        self.assertNotEqual(title, image_alt, "Link title and image alt are the same")
        
#    Currently alt tag is not required, nor does it appear for most messages. Uncomment if alt tag is used frequently
#    def testPresentsOfImage(self):
#        src = self.driver.find_element_by_css_selector(".hpLeadImg img").get_attribute("alt")
#        assert (len(src) > 0), "Empty alt description. Image can be missed"
        
    def testSeeMore(self):
        a = self.driver.find_elements_by_css_selector(".mod.line.newsBlock .modHeader")
        for i in a: 
            key = i.find_element_by_tag_name("h2").text
            value =  i.find_element_by_tag_name("a").get_attribute("href")
            if not SEEMORE[key] == value:
                print SEEMORE[key],  value
                self.assertEqual(1, 2, "See all url doesn't match the text")         
            
    
    def testFooter(self):
        sub_menus = self.driver.find_elements_by_css_selector(".unit.netLinks")
        all_url = []
        device_name = mobile_util.get_device_name()
        if device_name.__contains__('phone'):
            for sub_group in sub_menus:
                column = []
                url_category = sub_group.find_element_by_tag_name("a").get_attribute("href")
                column.append(url_category)
                list_of_li = sub_group.find_elements_by_css_selector(".netLink")
                for i in list_of_li:
                    link_displayed = i.is_displayed()
                    self.assertEqual(link_displayed, False, "Footer links appear for mobile devices but should not appear")
        else:
            for sub_group in sub_menus:
                column = []
                url_category = sub_group.find_element_by_tag_name("a").get_attribute("href")
                column.append(url_category)
                list_of_li = sub_group.find_elements_by_css_selector(".netLink")
                for i in list_of_li:
                    line_url = i.get_attribute("href")
                    line_text = i.text
                    #column.append(line_url)
                    column.append(line_text)
                all_url.append(column)
            print "New", all_url
            self.assertEqual(all_url, FOOTER, "Footer has been changed. URLs or Text changed")
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(HomepageTestCase)
    unittest.TextTestRunner().run(suite)