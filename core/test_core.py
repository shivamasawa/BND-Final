from selenium import webdriver
import unittest
import sys
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from configs.config import CHROME_PATH, CHROME_BETA_BINARY, FF_PATH, EDGE_PATH, HEADLESS_CHROME_PATH
import utils.env_util as env_util

class TestCore(unittest.TestCase):
    
    driver = None
    
    @classmethod
    def setUpClass(cls):
        super(TestCore, cls).setUpClass()
        # profile = webdriver.FirefoxProfile('C:\\Users\\shizuleuski\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\dfyhvard.default')
        browser_name = env_util.get_browser();
        if(browser_name == 'chrome'):
            options = webdriver.ChromeOptions()
            options.add_argument('chrome')
            TestCore.driver = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=options)
            TestCore.driver.set_window_size(1280,800)
        elif (browser_name == "chrome"):
            TestCore.driver = webdriver.Chrome(CHROME_PATH)
        elif (browser_name == "chrome_beta"):
            options = webdriver.ChromeOptions()
            options.binary_location = CHROME_BETA_BINARY
            TestCore.driver = webdriver.Chrome(executable_path=CHROME_PATH, chrome_options=options)
        elif (browser_name == "firefox"):
            firefox_capabilities = DesiredCapabilities.FIREFOX
            firefox_capabilities['marionette'] = True
            TestCore.driver = webdriver.Firefox(capabilities=firefox_capabilities, executable_path=FF_PATH)
        elif (browser_name == "safari"):
            TestCore.driver = webdriver.Safari()
        elif (browser_name == "edge"):
            TestCore.driver = webdriver.Edge(EDGE_PATH)
        TestCore.driver.implicitly_wait(10)
        TestCore.driver.set_page_load_timeout(90)
        TestCore.driver.maximize_window()
        TestCore.driver.switch_to
        # self.driver.maximize_window()
     
    def setUp(self):
        self.driver = TestCore.driver
            
    @classmethod
    def tearDownClass(cls):
        TestCore.driver.quit()
        super(TestCore, cls).tearDownClass()