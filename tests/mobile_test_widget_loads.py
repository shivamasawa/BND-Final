import unittest
import sys
import os
import time
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util

WEB_SITE = env_util.get_env_url()

def verifyWidgetWidget(self, numWidgets):
        widgets = self.driver.find_elements_by_css_selector('.bz__RfqWidget')
        self.assertTrue(len(widgets) == numWidgets, '[Current: '+str(len(widgets))+' widgets] [Expected: '+str(numWidgets)+' widgets]')
        for widget in widgets:
            self.assertTrue(widget.is_displayed(), 'Widget is not displayed')
            question = self.driver.find_element_by_css_selector('.bz__Question')
            self.assertTrue(question.is_displayed(), 'Question is not displayed')
            answer = self.driver.find_element_by_css_selector('.bz__AnswerLabel')
            self.assertTrue(answer.is_displayed(), 'Answer is not displayed')
            #next_button = self.driver.find_element_by_css_selector('#btnNext')
            #self.assertTrue(next_button.is_displayed(), 'Next Button is not displayed')

class WidgetTestCase(mobile_test_core.MobileTestCore):
   
    @classmethod
    def setUpClass(cls):
        super(WidgetTestCase, cls).setUpClass()
        driver = mobile_test_core.MobileTestCore.driver
        
    def testArticleOptimizedFranchises(self):
        url = WEB_SITE + '5317-part-time-franchises.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 1)
    
    def testArticleOptimizedMailingEquipment(self):
        url = WEB_SITE + '7052-mailing-equipment-solutions.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 1)
    
    def testBestPickCreditCards(self):
        url = WEB_SITE + '8061-best-credit-card-processing.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 2)
        
    def testBestBusinessPhone(self):
        url = WEB_SITE + '6780-best-business-phone-systems.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 2)
    
    def testSkyBestPicksCRMSoftware(self):
        url = WEB_SITE + '7839-best-crm-software.html?orchId=1794'
        print(url)
        self.driver.get(url)
        try:
            verifyWidgetWidget(self, 2)
        except:
            time.sleep(1)
            verifyWidgetWidget(self, 2)
        
    def testBuyingGuideBusinessPhone(self):
        url = WEB_SITE + '7149-business-phone-system-guide.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 2)
        
    def testSlideShowBusinessIdeas1(self):
        url = WEB_SITE + '2747-great-business-ideas.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 1)
        
    def testSlideShowBusinessIdeas2(self):
        url = WEB_SITE + '1878-business-business-ideas.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 1)
        
    def testSlideShowBusinessIdeas2012(self):
        url = WEB_SITE + '1646-great-business-ideas-2012.html'
        print(url)
        self.driver.get(url)
        verifyWidgetWidget(self, 1)
    
#    def testReferenceCosts(self):
#        url = WEB_SITE + '5498-direct-costs-indirect-costs.html'
#        self.driver.get(url)
#        verifyWidgetWidget(self, 1)
        
    def testReferenceCashFlow(self):
        url = WEB_SITE + '4635-cash-flow-management.html'
        print(url)
        self.driver.get(url)
        try:
            verifyWidgetWidget(self, 1)
        except AssertionError as err:
            env = env_util.get_env()
            if ("prod" in env):
                raise err;
    
#    def testReferenceOptimizedBusinessPlan(self):
#        url = WEB_SITE + '4533-business-plan-outline.html'
#        print(url)
#        self.driver.get(url)
#        verifyWidgetWidget(self, 2)
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    unittest.TextTestRunner().run(suite) 
    