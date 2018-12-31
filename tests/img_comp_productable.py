from selenium import webdriver
from needle.cases import NeedleTestCase
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import utils.env_util as env_util

WEB_SITE = env_util.get_env_url()

class ProductTableTest(NeedleTestCase):
    # run with nosetests img_comp_productable.py --with-save-baseline for baseleine 
    
    def test_search(self):
        self.driver.maximize_window()
        self.driver.get("https://www.businessnewsdaily.com/7543-best-accounting-software.html")
        self.assertScreenshot('.productGrid', 'product_table')

    def testLogoUnit(self):
        self.driver.maximize_window()
        self.driver.get(WEB_SITE)
        self.assertScreenshot('.mqMedOff', 'logo')

    def testBIGgenerator(self):
        self.driver.maximize_window()
        TEST_URL = WEB_SITE + "3253-business-idea-generator.html"
        self.driver.get(TEST_URL)
        self.assertScreenshot('#quiz_img', 'big_logo')

    def testNavigationMenu(self):
        self.driver.maximize_window()
        self.driver.get(WEB_SITE)
        self.assertScreenshot('.siteNav.unit', 'navigation')

    def testFooterLogo(self):
        self.driver.maximize_window()
        self.driver.get(WEB_SITE)
        self.assertScreenshot('.mod>a>img', 'footer_logo')
        
    
    def testCountdownImage(self):
        self.driver.maximize_window()
        COUNTDOWN_URL = WEB_SITE + "7162-best-smartphones.html"
        self.driver.get(COUNTDOWN_URL)
        self.assertScreenshot('.articleBody>img', 'article_image')
        
      
    def testOptimizedPage(self):
        self.driver.maximize_window()
        COUNTDOWN_URL = WEB_SITE + "6780-best-business-phone-systems.html"
        self.driver.get(COUNTDOWN_URL)
        self.assertScreenshot('.thumbRight>img', 'optimized_image')
        
      
    def testImageLargeArticle(self):
        self.driver.maximize_window()
        ARTICLE_URL = WEB_SITE + "4659-what-is-roi.html"
        self.driver.get(ARTICLE_URL)
        self.assertScreenshot('.thumbRight>img', 'huge_article_image')
        
        
        

        
        
        