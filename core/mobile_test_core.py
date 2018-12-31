from appium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import utils.mobile_util as mobile_util


class MobileTestCore(unittest.TestCase):
    device_name = ""
    driver = None
    
    @classmethod
    def setUpClass(cls):
        super(MobileTestCore, cls).setUpClass()
        MobileTestCore.device_name = mobile_util.get_device_name()
        desired_caps = mobile_util.get_desired_capabilities(cls.device_name)
        MobileTestCore.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        MobileTestCore.driver.implicitly_wait(10)
        MobileTestCore.driver.set_page_load_timeout(90)

    def setUp(self):
        self.driver = MobileTestCore.driver
        self.driver.switch_to
        self.device_name = MobileTestCore.device_name
        
    @classmethod
    def tearDownClass(cls):
        if MobileTestCore.driver != None:
            MobileTestCore.driver.quit()
        super(MobileTestCore, cls).tearDownClass()