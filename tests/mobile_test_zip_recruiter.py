#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import random
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import mobile_test_core
from utils import env_util, mobile_util

WEB_SITE = env_util.get_env_url()
ARTICLES = ['4968-best-jobs-for-future.html','4975-choosing-the-best-job.html','9264-follow-up-after-job-interview.html']

def verifyElementIsDisplayedAndSpansWidth(self, web_element):
    browser_width = mobile_util.get_browser_width(self.device_name, self.driver)
    print('Browser width: '+str(browser_width))
    width = web_element.size.get('width')
    print('Element width: '+str(width))
    assert (width <= browser_width) and (width >= (browser_width - 110))
    
class ZipRecruiterTestCase(mobile_test_core.MobileTestCore):
        
    def testZipRecruiterLoads(self):
        for article in ARTICLES:
            url = WEB_SITE+article
            self.driver.get(url)
            try:
                zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
                assert zip_recruiter_box.is_displayed() == True
            except:
                print(self.driver.current_url)
                self.driver.refresh()
                time.sleep(3)
                zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
                assert zip_recruiter_box.is_displayed() == True
            if('phone' in self.device_name):
                verifyElementIsDisplayedAndSpansWidth(self, zip_recruiter_box)
            job_links = zip_recruiter_box.find_elements_by_css_selector('.zr_job_title')
            num_job_links = len(job_links)
            self.assertEquals(num_job_links, 3, 'Number of job links was not 3')
            for link in job_links:
                self.assertTrue(link.is_displayed(), 'At lease one of job links was not displayed')
            job_details = zip_recruiter_box.find_elements_by_css_selector('.zr_job_details')
            num_job_details = len(job_details)
            self.assertEquals(num_job_details, 3, 'Number of job details was not 3')
            for detail in job_details:
                self.assertTrue(detail.is_displayed(), 'At lease one of job links was not displayed')
            zip_logos = self.driver.find_elements_by_css_selector('#zr_attributed')
            num_logos = len(zip_logos)
            self.assertEquals(num_logos, 1, 'Number of zip recruiter logos was not 1')
            self.assertTrue(zip_logos[0].is_displayed(), 'Zip recruiter logo is not displayed')
            more_jobs = self.driver.find_element_by_css_selector('#zip-button')
            self.assertTrue(more_jobs.is_displayed(), 'More jobs button is not displayed')
            
    def testZipRecruiterLink(self):
        url = WEB_SITE+ARTICLES[random.randint(0, len(ARTICLES)-1)]
        self.driver.get(url)
        zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
        job_links = zip_recruiter_box.find_elements_by_css_selector('.zr_job_link')
        link = job_links[random.randint(0, len(job_links)-1)]
        self.driver.execute_script("return arguments[0].scrollIntoView();", link)
        if 'phone' in self.device_name:
            self.driver.execute_script("window.scrollBy(0,-500)")
            self.driver.execute_script("return arguments[0].scrollIntoView();", link)
        if('android' in self.device_name):
                link.click()
        else:
            mobile_util.tap_webview_element(self.driver, self.device_name, link)
        time.sleep(3)
        if 'android' in self.device_name:
            handles = self.driver.window_handles
            new_handle = handles[1]
            self.driver.switch_to.window(new_handle)
        else:
            handles = self.driver.contexts
            new_handle = handles[2]
            self.driver.switch_to.context(new_handle)
        zip_url = self.driver.current_url
        assert zip_url != u''+url
        self.driver.close()
        if 'android' in self.device_name:
            self.driver.switch_to.window(handles[0])
        else:
            self.driver.switch_to.context(handles[1])
        
    def testSeeMoreJobs(self):
        url = WEB_SITE+ARTICLES[random.randint(0, len(ARTICLES)-1)]
        self.driver.get(url)
        see_more = self.driver.find_element_by_css_selector('#zip-button')
        self.driver.execute_script("return arguments[0].scrollIntoView();", see_more)
        if 'phone' in self.device_name:
            self.driver.execute_script("window.scrollBy(0,-500)")
            time.sleep(1)
            self.driver.execute_script("return arguments[0].scrollIntoView();", see_more)
        if('android' in self.device_name):
            see_more.click()
        else:
            time.sleep(2)
            mobile_util.tap_webview_element(self.driver, self.device_name, see_more)
        time.sleep(3)
        if 'android' in self.device_name:
            handles = self.driver.window_handles
            new_handle = handles[1]
            self.driver.switch_to.window(new_handle)
        else:
            handles = self.driver.contexts
            new_handle = handles[2]
            self.driver.switch_to.context(new_handle)
        zip_url = self.driver.current_url
        assert zip_url == u''+WEB_SITE+'ziprecruiter.html'
        assert self.driver.find_element_by_id('zs_search_module').is_displayed() == True
        assert self.driver.find_element_by_id('zs_search').is_displayed() == True
        assert self.driver.find_element_by_id('zs_location').is_displayed() == True
        assert self.driver.find_element_by_id('zs_radius').is_displayed() == True
        assert self.driver.find_element_by_id('zs_days').is_displayed() == True
        assert self.driver.find_element_by_id('zs_submit').is_displayed() == True
        results = self.driver.find_elements_by_css_selector('.zr_job')
        assert len(results) > 0
        if('phone' in self.device_name):
            verifyElementIsDisplayedAndSpansWidth(self, self.driver.find_element_by_id('zs_search_module'))
        self.driver.close()
        if 'android' in self.device_name:
            self.driver.switch_to.window(handles[0])
        else:
            self.driver.switch_to.context(handles[1])
        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ZipRecruiterTestCase)
    unittest.TextTestRunner().run(suite)