#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import random
import time
import sys
import os
from selenium.common.exceptions import WebDriverException
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
import utils.env_util as env_util


WEB_SITE = env_util.get_env_url()
ARTICLES = ['4968-best-jobs-for-future.html','4975-choosing-the-best-job.html',
            '9264-follow-up-after-job-interview.html','2389-jobs-travel-lovers.html','5126-best-jobs-introverts.html']

    
class ZipRecruiterTestCase(test_core.TestCore):
        
    def testZipRecruiterLoads(self):
        for article in ARTICLES:
            url = WEB_SITE+article
            self.driver.get(url)
            zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
            time.sleep(2)
            self.assertTrue(zip_recruiter_box.is_displayed(), 'Zip recruiter box is not displayed on '+url)
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
        time.sleep(1)
        link.click()
        time.sleep(2)
        handles = self.driver.window_handles
        try:
            new_handle = handles[1]
            self.driver.switch_to.window(new_handle)
        except:
            time.sleep(3)
            link.click()
            time.sleep(2)
            handles = self.driver.window_handles
            new_handle = handles[1]
        zip_url = self.driver.current_url
        assert zip_url != url
        self.driver.close()
        self.driver.switch_to.window(handles[0])
        
    def testSeeMoreJobs(self):
        url = WEB_SITE+ARTICLES[random.randint(0, len(ARTICLES)-1)]
        self.driver.get(url)
        see_more = self.driver.find_element_by_css_selector('#zip-button')
        try:
            see_more.click()
            time.sleep(2)
            handles = self.driver.window_handles
            new_handle = handles[1]
            self.driver.switch_to.window(new_handle)
        except:
            time.sleep(3)
            see_more.click()
            time.sleep(2)
            handles = self.driver.window_handles
            new_handle = handles[1]
        self.driver.switch_to.window(new_handle)
        zip_url = self.driver.current_url
        print zip_url
        self.assertEquals(zip_url, WEB_SITE+'ziprecruiter.html', "Zip URL {0} doesn't match expected URL {1}".format(zip_url, WEB_SITE+'ziprecruiter.html'))
        print zip_url
        assert self.driver.find_element_by_id('zs_search_module').is_displayed() == True
        assert self.driver.find_element_by_id('zs_search').is_displayed() == True
        assert self.driver.find_element_by_id('zs_location').is_displayed() == True
        assert self.driver.find_element_by_id('zs_radius').is_displayed() == True
        assert self.driver.find_element_by_id('zs_days').is_displayed() == True
        assert self.driver.find_element_by_id('zs_submit').is_displayed() == True
        results = self.driver.find_elements_by_css_selector('.zr_job')
        assert len(results) > 0
        self.driver.close()
        self.driver.switch_to.window(handles[0])

        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ZipRecruiterTestCase)
    unittest.TextTestRunner().run(suite)