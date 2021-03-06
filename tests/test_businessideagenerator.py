#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util, webdriver_util #,ad_util

# profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
# driver = webdriver.Firefox(profile)

BIG_URL = env_util.get_env_url() + "3253-business-idea-generator.html"
browsers = {"firefox": webdriver.Firefox, "ie": webdriver.Ie, "chrome": webdriver.Chrome}
#TEXT_FIRST_SLIDE = "Based on your responses, you may be a good fit to own and operate a retail store. Owning a retail, whether it's selling clothes, books, or furniture, will require a large investment. In also will mean you will need to hire employees and manage them successfully. Since most retail owners are very hands-on, it will give you the chance work with customers on a daily basis and show off your salesperson skills. After seeing a number of businesses go under during the recession, some may have doubts on how successful a retail store can be. Despite a lingering economic uncertainty, research from the U.S. Census Bureau shows Americans are spending again. Overall retail sales in July were up 4.1 percent from a year ago, with certain types of retail doing even better. Sporting goods, hobby, book and music stores saw sales increase by more than 10 percent from last year. The retail industry gives you all sorts of business options. The North American Industry Classification System has identified nearly 70 different types of retail ventures. Jewelry, art, auto parts, office supplies, luggage, clothing, souvenirs, food, hardware and computers can all be sold from a retail location."
#TEXT_FIRST_SLIDE_PAR1 = "Based on your responses, your interests and goals closely align with a business that offers writing, marketing and other creative services. This is an ideal fit for anyone from a creative background, such as art, writing, graphic design, film, public relations, architecture, event planning, and photography. Additionally, this benefits anyone looking to work remotely, since creatives operate from their homes. You have the freedom to work exclusively for yourself, on your own schedule and at your own pace."
#TEXT_FIRST_SLIDE_PAR2 = "As of January 2015, there were 702,771 businesses employing 2.9 million creatives in the United States, Americans for the Arts reported. There is a need for individuals who run creative-service businesses, and you could be one of them. According to the Creative Industry Report, nine out of 10 businesses on average can utilize a freelance employee. The same report mentions that 66 percent of businesses commission for photography and 55 percent utilize video-production services."
#TEXT_FIRST_SLIDE_PAR3 = "To establish your own creative-service business, you need internal motivation as a leader and a knack for business. The internet has created many ways for creatives to offer their talents and profit from their services. Many businesses, including online publications, want multimedia content that staff employees might not offer. Although you might consider yourself a freelancer, it might benefit you to establish yourself as an LLC, especially for tax benefits and if you plan to hire employees."
#TEXT_SECOND_SLIDE = "Based on your answer"
#TEXT_SECOND_SLIDE = "Based on your responses, you would be well-suited to the app-design industry."

class BIGTestCase(test_core.TestCore): 
         
    def testSwitchingToLatest(self):
        def go_to_the_last():
            self.driver.get(BIG_URL)
            #ad_util.verifyAdLoadsAndClose(self.driver)
            #for i in range(11):
            #    self.driver.execute_script("""$("#quiz_action").mousedown()""")
            start_button = self.driver.find_element_by_id("quiz_action")
            webdriver_util.scroll_to_element(self.driver, start_button)
            start_button.click()
            '''for i in range(10):
                answer = self.driver.find_element_by_xpath("//div[@class='inq_answer'][1]")
                webdriver_util.scroll_to_element(self.driver, answer)
                answer.click()
            self.driver.find_element_by_id("quiz_action").click()'''
        go_to_the_last()
        
        
    '''def testContent(self):
        a = BIGTestCase.testSwitchingToLatest(self)
        paragraphs = self.driver.find_elements_by_css_selector(".count_desc>p")
        #a = self.driver.find_element_by_css_selector(".count_desc>p").text 
        a = paragraphs[0].text
        self.assertEqual(a, TEXT_FIRST_SLIDE_PAR1, "{0} doesn't match".format(a))
        a = paragraphs[1].text
        self.assertEqual(a, TEXT_FIRST_SLIDE_PAR2, "{0} doesn't match".format(a))
        a = paragraphs[2].text
        self.assertEqual(a, TEXT_FIRST_SLIDE_PAR3, "{0} doesn't match".format(a))
        
    def testNextSlide(self):
        BIGTestCase.testSwitchingToLatest(self)
        next_button = self.driver.find_element_by_css_selector("#countdown_next>span")
        webdriver_util.scroll_to_element(self.driver, next_button)
        next_button.click()
        a = self.driver.find_element_by_css_selector(".count_desc>p").text[:77]
        self.assertEqual(a, TEXT_SECOND_SLIDE, "{0} doesn't match".format(a))'''
    
if __name__ == "__main__":
    browsername = "firefox"
    # unittest.main(verbosity=2)
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    #browser = browsers[browsername]

    suite = unittest.TestLoader().loadTestsFromTestCase(BIGTestCase)
    unittest.TextTestRunner().run(suite)
