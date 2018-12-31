import unittest
import time
import test_mobile_core

WEB_SITE = "https://www.businessnewsdaily.com/"

def verifyWidgetWidget(self, numWidgets):
        try:
            widgets = self.driver.find_elements_by_css_selector('.bz__RfqWidget')
            self.assertTrue(len(widgets) == numWidgets, '[Current: '+str(len(widgets))+' widgets] [Expected: '+str(numWidgets)+' widgets]')
        except:
            time.sleep(3)
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

class WidgetTestCase(test_mobile_core.MobileTestCore):
   
    @classmethod
    def setUpClass(cls):
        super(WidgetTestCase, cls).setUpClass()
        driver = test_mobile_core.MobileTestCore.driver
        
    def testWidgetsLoad(self):
        print("================ Widget Loading Tests ================")
        errors = []
        #testArticleOptimizedFranchises
        try:
            url = WEB_SITE + '5317-part-time-franchises.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 1)
            print("testArticleOptimizedFranchises: pass")
        except Exception as err:
            print("testArticleOptimizedFranchises: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testArticleOptimizedMailing
        try:
            url = WEB_SITE + '7052-mailing-equipment-solutions.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 1)
            print("testArticleOptimizedMailing: pass")
        except Exception as err:
            print("testArticleOptimizedMailing: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testBestPickCreditCards
        try:
            url = WEB_SITE + '8061-best-credit-card-processing.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 2)
            print("testBestPicksCreditCards: pass")
        except Exception as err:
            print("testBestPicksCreditCards: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testBestBusinessPhone
        try:
            url = WEB_SITE + '6780-best-business-phone-systems.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 2)
            print("testBestPicksBusiessPhone: pass")
        except Exception as err:
            print("testBestPicksBusinessPhone: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testSkyBestPicksCRMSoftware
        try:
            url = WEB_SITE + '7839-best-crm-software.html?orchId=1794'
            self.driver.get(url)
            verifyWidgetWidget(self, 2)
            print("testSkyBestPicksCRMSoftware: pass")
        except Exception as err:
            print("testSkyBestPicksCRMSoftware: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testBuyingGuideBusinessPhone
        try:
            url = WEB_SITE + '7149-business-phone-system-guide.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 2)
            print("testBuyingGuideBusinessPhone: pass")
        except Exception as err:
            print("testBuyingGuideBusinessPhone: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testSlideShowBusinessIdeas1
        try:
            url = WEB_SITE + '2747-great-business-ideas.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 1)
            print("testSlideShowBusinessIdeas1: pass")
        except Exception as err:
            print("testSlideShowBusinessIdeas1: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testSlideShowBusinessIdeas2
        try:
            url = WEB_SITE + '1878-business-business-ideas.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 1)
            print("testSlideShowBusinessIdeas2: pass")
        except Exception as err:
            print("testSlideShowBusinessIdeas2: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
        
        #testSlideShowBusinessIdeas2012
        try:
            url = WEB_SITE + '1646-great-business-ideas-2012.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 1)
            print("testSlideShowBusinessIdeas2012: pass")
        except Exception as err:
            print("testSlideShowBusinessIdeas2012: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testReferenceCosts
#        try:
#            url = WEB_SITE + '5498-direct-costs-indirect-costs.html'
#            self.driver.get(url)
#            verifyWidgetWidget(self, 1)
#            print("testReferenceCosts: pass")
#        except Exception as err:
#            print("testReferenceCosts: FAIL")
#            print(self.driver.current_url)
#            print(err)
#            errors.append(err)
#        print("---------------------------------------------------")
        
        #testReferenceCashFlow
        try:
            url = WEB_SITE + '4635-cash-flow-management.html'
            self.driver.get(url)
            verifyWidgetWidget(self, 1)
            print("testReferenceCashFlow: pass")
        except Exception as err:
            print("testReferenceCashFlow: FAIL")
            print(self.driver.current_url)
            print(err)
            errors.append(err)
        print("---------------------------------------------------")
    
        #testReferenceOptimizedBusinessPlan
#        try:
#            url = WEB_SITE + '4533-business-plan-outline.html'
#            self.driver.get(url)
#            verifyWidgetWidget(self, 2)
#            print("testReferenceOptimizedBusinessPlan: pass")
#        except Exception as err:
#            print("testReferenceOptimizedBusinessPlan: FAIL")
#            print(self.driver.current_url)
#            print(err)
#            errors.append(err)
#        print("---------------------------------------------------")
        
        
        if(len(errors) > 0):
            print("Total Failures/Errors: "+str(len(errors)))
            print("===================================================")
            raise errors[0]
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    unittest.TextTestRunner().run(suite) 
    