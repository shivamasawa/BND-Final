import unittest
import sys
import os
import time
import random
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util

WEB_SITE = env_util.get_env_url()
PATHS_2_ADS = ["6780-best-business-phone-systems.html","7819-best-phone-system-small-business.html",
         "7818-best-phone-system-small-office.html","7816-best-phone-system-call-center.html","8924-voip-for-business.html",
         "5706-best-online-fax-services.html","7914-best-online-fax-service-small-business.html",
         "7915-best-free-online-fax-service.html","7916-best-pay-per-use-online-fax-service.html","8968-best-secure-online-fax-service.html",
         "7912-choosing-an-online-fax-service.html","9556-best-video-conference-services.html","9859-best-video-phone-conferencing-collaboration-tools.html"]
PATHS_3_ADS = ["9527-best-accounting-software-for-mac.html", "7543-best-accounting-software.html"]

def verifyAd(self, ad, ad_name, expected_size):
        has_error = False
        try:
            ad_iframe = ad.find_element_by_tag_name('iframe');
            self.driver.switch_to_frame(ad_iframe)
            ad_image = self.driver.find_element_by_css_selector("a>img")
            self.assertTrue(ad_image.is_displayed(), "Native ad is not displayed: "+ad_name)
            height = ad_image.value_of_css_property("height")
            dec_height = [str(s) for s in height.split("px") if s.isdigit()][0]
            width = ad_image.value_of_css_property("width")
            dec_width = [str(s) for s in width.split("px") if s.isdigit()][0]
            size = dec_width +"x" + dec_height
            #print size, "size"
            self.assertEquals(size, expected_size, 'Ad is not correct size - expected '+size+' for '+ad_name)
        except Exception as e:
            has_error = True
        finally:
            self.driver.switch_to_default_content()
            if(has_error):
                raise e
        
class NativeAdsTestCase(test_core.TestCore):
   
    @classmethod
    def setUpClass(cls):
        super(NativeAdsTestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        
    def testNativeWith2Ads(self):
        url = WEB_SITE+PATHS_2_ADS[random.randint(0, len(PATHS_2_ADS)-1)]
        print(url)
        self.driver.get(url)
        ad1 = self.driver.find_element_by_id('in-article-vca-1')
        verifyAd(self, ad1, 'in-article-vca-1', '930x140')
        ad2 = self.driver.find_element_by_id('in-article-vca-2')
        verifyAd(self, ad2, 'in-article-vca-2', '930x490')
        
        
    def testNativeWith3Ads(self):
        url = WEB_SITE+PATHS_3_ADS[random.randint(0, len(PATHS_3_ADS)-1)]
        print(url)
        self.driver.get(url)
        top_ad = self.driver.find_element_by_id('ad_leaderboard')
        verifyAd(self, top_ad, 'ad_leaderboard', '930x240')
        ad1 = self.driver.find_element_by_id('in-article-vca-1')
        self.assertTrue(ad1.is_displayed(), "First native ad is not displayed")
        verifyAd(self, ad1, 'in-article-vca-1', '930x490')
        ad2 = self.driver.find_element_by_id('in-article-vca-2')
        verifyAd(self, ad2, 'in-article-vca-2', '930x140')
        
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(NativeAdsTestCase)
    unittest.TextTestRunner().run(suite) 
        