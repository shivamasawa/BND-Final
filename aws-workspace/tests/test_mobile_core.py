from appium import webdriver
import unittest

class MobileTestCore(unittest.TestCase):
    device_name = ""
    driver = None
    
    @classmethod
    def setUpClass(cls):
        super(MobileTestCore, cls).setUpClass()
        desired_caps = {}
        MobileTestCore.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        MobileTestCore.driver.implicitly_wait(10)
        MobileTestCore.driver.set_page_load_timeout(90)

    def setUp(self):
        self.driver = MobileTestCore.driver
        self.driver.switch_to
        #self.device_name = mobile_util.get_device_name() #NEED TO ADD THIS FUNCTION
        
    @classmethod
    def tearDownClass(cls):
        if MobileTestCore.driver != None:
            MobileTestCore.driver.quit()
        super(MobileTestCore, cls).tearDownClass()