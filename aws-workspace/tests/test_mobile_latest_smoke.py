#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import time
from datetime import date, timedelta
from selenium.webdriver.common.action_chains import ActionChains
import test_mobile_core
import webdriver_util

WEB_SITE = "https://www.businessnewsdaily.com/"
COUNTDOWNS = "Countdown"
IMAGE_ALBUM = "Image Album"
REFERENCE = "Reference" 
LATEST = WEB_SITE + "latest"
NEWSLETTER = WEB_SITE + "newsletter"
THANKS = "Thank you"

class LatestTestCase(test_mobile_core.MobileTestCore):
    
    def testLatest(self): 
        print("================ Latest Page Test ================")
        errors = []
        #testSwitchingToLatest
        try:
            self.driver.get(WEB_SITE)
            time.sleep(30)
            field = self.driver.find_element_by_css_selector(".hpLatestHeadlines")
            self.driver.execute_script("return arguments[0].scrollIntoView();", field)
            field.click()
            current_url = self.driver.current_url
            #print current_url 
            print("testLatest: pass")
        except Exception as err:
            print("testLatest: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testRecentNews
        try:
            self.driver.get(LATEST)
            #print time.strftime("%B %d, %Y")
            today = time.strftime("%B %d, %Y")
            full_text = self.driver.find_element_by_css_selector(".date-posted").text
            full_text.encode('ascii','ignore')
            i = full_text.find(" | ") 
            #print full_text[:i]
            date_from_page = full_text[:i]
            #Check that any recent news were published today.test can fail on Monday's morning .
            #More complicated logic should be applied 
            try:
                self.assertEqual(date_from_page, today, "Latest wasn't updated today. It COULD be a problem")
            except:
                yesterday = date.today() - timedelta(1)
                yesterday = yesterday.strftime("%B %d, %Y")
                self.assertEqual(date_from_page, yesterday, "Latest wasn't updated today or yesterday. It COULD be a problem")
            print("testRecentNews: pass")
        except Exception as err:
            print("testRecentNews: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testFilterTypeCountdown:
        try:
            self.driver.get(LATEST)
            self.driver.find_element_by_css_selector(".filter-label.mqMedOn").click()
            elem = self.driver.find_element_by_css_selector(".filter-list li:nth-of-type(3) a")
            def hover(elem):
                hov = ActionChains(self.driver).move_to_element(elem)
                hov.perform()   
            elem.click()
            time.sleep(3)
            full_text_all = self.driver.find_elements_by_css_selector(".date-posted")
            for full_text in full_text_all:
                text_value = full_text.text
                content_type =  text_value[text_value.find(" | ") + 3:]
                self.assertEqual(content_type, COUNTDOWNS, "Content not valid")
            print("testFilterTypeCountdown: pass")
        except Exception as err:
            print("testFilterTypeCountdown: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
            
        #testFilterTypeReference
        try:
            self.driver.get(LATEST)
            self.driver.find_element_by_css_selector(".filter-label.mqMedOn").click()
            elem = self.driver.find_element_by_css_selector(".filter-list li:nth-of-type(5) a")
            def hover(elem):
                hov = ActionChains(self.driver).move_to_element(elem)
                hov.perform()   
            elem.click()
            time.sleep(3)
            full_text_all = self.driver.find_elements_by_css_selector(".date-posted")
            for full_text in full_text_all:
                text_value = full_text.text
                content_type =  text_value[text_value.find(" | ") + 3:]
                self.assertEqual(content_type, REFERENCE, "Content not valid")   
            print("testFilterTypeReference: pass")
        except Exception as err:
            print("testFilterTypeReference: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")     
   
        #testSecondPage
        try:
            self.driver.get(LATEST)
            elem = self.driver.find_element_by_css_selector("a.unit-pagination[href*='/latest/2']")
            webdriver_util.scroll_to_element(self.driver, elem)
            elem.click()
            time.sleep(2)
            current_url = self.driver.current_url
            second_page = LATEST + "/2"
            #print "THe current url is {0}, and latest is {1}".format(current_url, second_page) 
            self.assertEqual(current_url, second_page, "Didn't change the page {0} doesn't match \n {1}".format(current_url, second_page))   
            print("testSecondPage: pass")
        except Exception as err:
            print("testSecondPage: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")  
        if(len(errors) > 0):
            print("Total Failures/Errors: "+str(len(errors)))
            print("===================================================")
            raise errors[0] 
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(LatestTestCase)
    unittest.TextTestRunner().run(suite)