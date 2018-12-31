#!/usr/bin/python
# -*- coding: UTF-8 -*-
          
import unittest
import test_mobile_core

WEB_SITE = "https://www.businessnewsdaily.com/8193-working-moms-stress.html"
ONE = "Build Your Career"
TWO = "Work-Life Balance"
AUTHOR = "Brittney Morgan, Business News Daily Contributing Write"
TIME_STAMP = """July 14, 2015 09:23 am EST"""
YOUMAYLIKE = "You May Also like"

class ArticleTestCase(test_mobile_core.MobileTestCore):
    
    @classmethod
    def setUpClass(cls):
        super(ArticleTestCase, cls).setUpClass()
        driver = test_mobile_core.MobileTestCore.driver
        try:
            driver.get(WEB_SITE)
        except Exception as e:
            driver.quit()
            raise e
    
    def testArticlePage(self):
        print("================ Article Page Test ================")
        errors = []
        #testCrumb
        try:
            lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child").text
            lv_one = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:first-child").text
            self.assertEquals(lv_one, ONE, "One {0} doesn't match the {1}".format(lv_one, ONE))
            self.assertEquals(lv_two, TWO, "Two {0} doesn't match the {1}".format(lv_two, TWO))
            print("testCrumb: pass")
        except Exception as err:
            print("testCrumb: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        #testTimestamp
        try:
            author = self.driver.find_element_by_class_name("author").text
            time_stamp = self.driver.find_element_by_css_selector(".byline time").text
            self.assertEquals(author, AUTHOR, "author {0} doesn't match the {1}".format(author, AUTHOR))
            self.assertEquals(time_stamp, TIME_STAMP, "Time {0} doesn't match the {1}".format(time_stamp, TIME_STAMP))
            print("testTimestamp: pass")
        except Exception as err:
            print("testTimestamp: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
       
        #testYouMayAlsoLike
        try:   
            youmaylike = self.driver.find_element_by_css_selector(".sideBar div").text 
            self.assertEquals(youmaylike.lower(), YOUMAYLIKE.lower(), "text {0} doesn't match the {1}".format(youmaylike, YOUMAYLIKE))
            print("testYouMayAlsoLike: pass")
        except Exception as err:
            print("testYouMayAlsoLike: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
       
        #testAnother
        try:
            lv_two = self.driver.find_element_by_css_selector(".crumbs.mod.topMod.article-crumb span:last-child>a")
            color = lv_two.value_of_css_property("color")
            self.assertEqual("rgba(0, 126, 204, 1)", color, "Bread crumps color was changed")
            print("testAnother: pass")
        except Exception as err:
            print("testAnother: FAIL")
            print("Error URL: "+self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        if(len(errors) > 0):
            print("Total Failures/Errors: "+str(len(errors)))
            print("===================================================")
            raise errors[0]
        
#    def testImageAlt(self):
#        h1 = self.driver.find_element_by_css_selector("h1")
#        h1_text = h1.text
#        image = self.driver.find_element_by_css_selector(".magnify-wrapper>img")
#        img_alt = image.get_attribute("alt")
#        self.assertNotEqual(h1_text, img_alt, "H1 and image alt are the same")
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ArticleTestCase)
    unittest.TextTestRunner().run(suite)
