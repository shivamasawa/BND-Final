import unittest
import sys
import os
import time
import datetime
import calendar
from time import strptime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
from utils import env_util
WEB_SITE = env_util.get_env_url()
BOOKING_MSG = "You're all done. "

class ScheduleAppointmentTestCase(test_core.TestCore):
    
    @classmethod
    def setUpClass(cls):
        super(ScheduleAppointmentTestCase, cls).setUpClass()
        driver = test_core.TestCore.driver
        try:
            driver.get(WEB_SITE+'2955-best-pos-systems.html')
        except Exception as e:
            driver.quit()
            raise e
        
    def testAppointment(self):
        appointmentBtn = self.driver.find_element_by_xpath("//a[@class='css-1rttg5 eptmmhg1']")
        appointmentBtn.click()
        time.sleep(5)
        iframe = self.driver.find_element_by_xpath("//iframe[@class='css-1023aa8 eptmmhg2']")
        self.driver.switch_to.frame(iframe)
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='calButtons']/button[2]").click()
        timeBtn = self.driver.find_element_by_xpath("//div[@class='times-section']/div[1]/ion-row/ion-col/div[2]/button")
        timeBtn.click()
        if self.driver.find_element_by_xpath("//ion-toast[@class='toast-md']").is_displayed():
            self.driver.find_element_by_xpath("//div[@class='calButtons']/button[1]").click()
            self.driver.find_element_by_xpath("//div[@class='cal-day-headers']/div[6]").click()
            self.driver.find_element_by_xpath("//div[@class='times-section']/div[1]/ion-row/ion-col/div[2]/button").click()
        time.sleep(3)
        date_time = self.driver.find_element_by_xpath("//div[@class='contentInfo info']/div/ion-nav/page-booking[1]/ion-content/div[2]/ion-row/form/div[1]/h3").text[4:]
        month_abr = date_time[:3]
        month_index = strptime(month_abr, '%b').tm_mon
        month_nme = calendar.month_name[month_index]
        expected_date = month_nme + date_time[3:]
        self.driver.find_element_by_xpath("//input[@name='firstname']").send_keys("test")
        self.driver.find_element_by_xpath("//input[@name='lastname']").send_keys("user")
        self.driver.find_element_by_xpath("//input[@name='email']").send_keys("testuser@gmail.com")
        self.driver.find_element_by_xpath("//input[@name='phone']").send_keys("5555555555")
        self.driver.find_element_by_xpath("//input[@class='validate text ng-untouched ng-pristine ng-invalid']").send_keys("testing")
        self.driver.find_element_by_xpath("//button[@class='btn blue bookingbutton complete']").click()
        time.sleep(3)
        booking_msg = self.driver.find_element_by_xpath("//div[@id='confTitle']/h1[1]").text
        booking_date = self.driver.find_element_by_xpath("//h3[@id='confTime']").text
        booking_num = self.driver.find_element_by_xpath("//h3[@id='confNumber']/span").text
        self.assertEquals(booking_msg, BOOKING_MSG, "Booking not Confirmed")
        self.assertTrue(booking_date == expected_date, "Incorrect Booking Date")
        self.assertIsNotNone(booking_num, "Booking Number is not generated")
        
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ScheduleAppointmentTestCase)
    unittest.TextTestRunner().run(suite) 