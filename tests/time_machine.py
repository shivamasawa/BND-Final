from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils import env_util
from configs.config import BROWSER_NAME, CHROME_PATH


WEB_SITE = env_util.get_env_url()

class TimeMachineTest(unittest.TestCase):
    # run with nosetests img_comp_homepage.py --with-save-baseline for baseleine 
    
    def setUp(self):
        # profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
        if (BROWSER_NAME == "chrome"):
            self.driver = webdriver.Chrome(CHROME_PATH)
        else:
            self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.set_page_load_timeout(90)
        self.driver.maximize_window()
        self.driver.switch_to
    def tearDown(self):
        self.driver.quit()
        
    def test_timemachine(self):
        directory = str(time.strftime("%m%d%Y"))
        folder = "TimeMachine/" + directory
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        self.driver.get(WEB_SITE + "")
        self.driver.save_screenshot(folder + "/homepage.png")
        
        self.driver.get(WEB_SITE + "7915-best-free-online-fax-service.html")
        self.driver.save_screenshot(folder + "/article01.png")
        # self.assertEqual(2, 3, "test")

        self.driver.get(WEB_SITE + "7319-mentorship-for-female-professionals.html")
        self.driver.save_screenshot(folder + "/article02.png")
        
        self.driver.get(WEB_SITE + "1136-corporate-it-consumer-technology-paradigm-shift-advantages-considerations.html")
        self.driver.save_screenshot(folder + "/article03.png")
        
        self.driver.get(WEB_SITE + "7543-best-accounting-software.html")
        self.driver.save_screenshot(folder + "/article_no_leaderboard.png")
        
        self.driver.get(WEB_SITE + "4993-creative-marketing-tactics.html")
        self.driver.save_screenshot(folder + "/countdown.png")   
        
        self.driver.get(WEB_SITE + "442-5-businesses-you-may-not-think-are-legal.html")
        self.driver.save_screenshot(folder + "/imagealbum.png")
        
        self.driver.get(WEB_SITE + "4813-contract-management.html")
        self.driver.save_screenshot(folder + "/reference.png")
        
        self.driver.get(WEB_SITE + "4893-workplace-quiz-test-your-office-knowledge.html")
        self.driver.save_screenshot(folder + "/quiz.png")
        
        self.driver.get(WEB_SITE + "start-your-business")
        self.driver.save_screenshot(folder + "/sectionpage01.png")
        
        self.driver.get(WEB_SITE + "grow-your-business")
        self.driver.save_screenshot(folder + "/sectionpage02.png")
        
        self.driver.get(WEB_SITE + "search?q=test+me")
        self.driver.save_screenshot(folder + "/search.png")
        
        self.driver.get(WEB_SITE + "latest?subsection=get-the-job")
        self.driver.save_screenshot(folder + "/latest.png")
        
        self.driver.get(WEB_SITE + "latest?type=article|countdown|image_album|references|countdown|image_album&subsection=get-the-job|get-ahead|office-life|work-life-balance|home-office")
        self.driver.save_screenshot(folder + "/latest2.png")
        
        self.driver.get(WEB_SITE + "newsletter")
        self.driver.save_screenshot(folder + "/newsletter.png")
        
        self.driver.get(WEB_SITE + "newsletter-signup")
        self.driver.save_screenshot(folder + "/signup.png")
        
        self.driver.get(WEB_SITE + "7707-best-ecommerce-software.html")
        self.driver.save_screenshot(folder + "/buerzone.png")
        
        self.driver.get(WEB_SITE + "wrongurl.html")
        self.driver.save_screenshot(folder + "/404.png")
        
        self.driver.get(WEB_SITE + "7319-mentorship-for-female-professionals.html")
        self.driver.save_screenshot(folder + "/article02.png")                                                                                                
         
        
        self.driver.get(WEB_SITE + "7509-best-payroll-services.html")
        self.driver.save_screenshot(folder + "/table02.png")                                                                                                
         
        self.driver.get(WEB_SITE + "7839-best-crm-software.html")
        self.driver.save_screenshot(folder + "/table01.png")                                                                                                
        
if __name__ == "__main__":
    #browsername = "firefox"
    #if len(sys.argv) == 2:
    #    browsername = sys.argv[1].lower()
    suite = unittest.TestLoader().loadTestsFromTestCase(TimeMachineTest)
    unittest.TextTestRunner().run(suite)
