#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util #, ad_util

# profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
# driver = webdriver.Firefox(profile)

QUIZ_URL = env_util.get_env_url() + "5004-job-interview-quiz.html"
TEXT_SCORE = "You Scored 0%"
TEXT_WELCOME = "Test your knowledge on what hiring managers expect during a job interview."

class QuizCase(mobile_test_core.MobileTestCore):
    
    def testGetTheScore(self):
        def go_to_the_last():
            self.driver.get(QUIZ_URL)
            #ad_util.verifyAdLoadsAndClose(self.driver)
            for i in range(11):
                self.driver.execute_script("""$("#quiz_action").mousedown()""")
            
        go_to_the_last()
        a = self.driver.find_element_by_class_name("score").text
        self.assertEqual(a, TEXT_SCORE, "{0} doesn't match {1}".format(a, TEXT_SCORE))
    
    def testStartOver(self):
        QuizCase.testGetTheScore(self)
        self.driver.find_element_by_css_selector("#restart_quiz>a").click()
        a = self.driver.find_element_by_css_selector("#quiz_info").text
        self.assertEqual(a, TEXT_WELCOME, "Start over button didn't change the slide")
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(QuizCase)
    unittest.TextTestRunner().run(suite)
