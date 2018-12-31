#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import random
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core import test_core
import utils.env_util as env_util


WEB_SITE = env_util.get_env_url()
ARTICLES = ['4968-best-jobs-for-future.html','4975-choosing-the-best-job.html','9264-follow-up-after-job-interview.html']
COUNTDOWNS = ['2389-jobs-travel-lovers.html','5126-best-jobs-introverts.html']

    
class ZipRecruiterTestCase(test_core.TestCore):
        
    def testZipRecruiterArticle(self):
        url = WEB_SITE+ARTICLES[random.randint(0, len(ARTICLES)-1)]
        print(url)
        self.driver.get(url)
        try:
            zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
            self.assertTrue(zip_recruiter_box.is_displayed(), 'Zip recruiter box is not displayed on '+url)
        except:
            time.sleep(3)
            zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
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
        
    def testZipRecruiterCountdown(self):
        url = WEB_SITE+COUNTDOWNS[random.randint(0, len(COUNTDOWNS)-1)]
        print(url)
        self.driver.get(url)
        try:
            zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
            self.assertTrue(zip_recruiter_box.is_displayed(), 'Zip recruiter box is not displayed on '+url)
        except:
            time.sleep(3)
            zip_recruiter_box = self.driver.find_element_by_css_selector('#zipsearch_container #zr_mini>div')
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
    
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(ZipRecruiterTestCase)
    unittest.TextTestRunner().run(suite)