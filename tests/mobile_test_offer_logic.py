import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util

WEB_SITE = env_util.get_env_url()

class OfferLogicTestCase(mobile_test_core.MobileTestCore):
   
    @classmethod
    def setUpClass(cls):
        super(OfferLogicTestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
        
#    def testBusinessLoans(self):
#        url = WEB_SITE+'8448-best-business-loans.html'
#        print(url)
#        self.driver.get(url)
#        offers = self.driver.find_elements_by_css_selector("div[id^='olcontent-grid'] div.aac-offer")
#        num_offers = len(offers)
#        self.assertEquals(num_offers, 4, "Expected 4 offers but found "+str(num_offers))
#        for offer in offers:
#            self.assertTrue(offer.is_displayed(), "At least 1 offer is not displayed")
        
        
#    def testSquareReview(self):
#        url = WEB_SITE+'8064-best-mobile-credit-card-processor.html'
#        print(url)
#        self.driver.get(url)
#        offer1 = self.driver.find_element_by_css_selector('div#olcontent-banner-1 div.aac-offer')
#        self.assertTrue(offer1.is_displayed(), "Header offer is not displayed")
#        offer2 = self.driver.find_element_by_css_selector('div#olcontent-howtobuy-1 div.aac-offer')
#        self.assertTrue(offer2.is_displayed(), "Content offer is not displayed")
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(OfferLogicTestCase)
    unittest.TextTestRunner().run(suite) 