import unittest
from tests.mobile_test_homepage import HomepageTestCase
from tests.mobile_test_latest_smoke import LatestTestCase
from tests.mobile_test_article import ArticleTestCase
from tests.mobile_test_optimized_template import OptimizedTemplateTestCase
from tests.mobile_test_widget_loads import WidgetTestCase
#from tests.mobile_test_offer_logic import OfferLogicTestCase
from tests.mobile_test_zip_recruiter_smoke import ZipRecruiterTestCase
from tests.mobile_test_countdown import CountdownTestCase

import utils.HTMLTestRunner as HTMLTestRunner
from utils.email_sender import mail
import tests.time_machine as time_machine
import os
from sys import argv
import sys
from configs.config import RESULTS_EMAIL
import utils.env_util as env_util
import utils.mobile_util as mobile_util

# run the nosetests img_comp_productable.py --with-save-baseline for the baseline images


def main(TimeMachine):
    
    homepage_tests = unittest.TestLoader().loadTestsFromTestCase(HomepageTestCase)
    latest_tests = unittest.TestLoader().loadTestsFromTestCase(LatestTestCase)
    article_tests = unittest.TestLoader().loadTestsFromTestCase(ArticleTestCase)
    optimized_template_tests = unittest.TestLoader().loadTestsFromTestCase(OptimizedTemplateTestCase)
    widget_tests = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    #offer_logic_tests = unittest.TestLoader().loadTestsFromTestCase(OfferLogicTestCase)
    zip_recruiter_tests = unittest.TestLoader().loadTestsFromTestCase(ZipRecruiterTestCase)
    countdown_tests = unittest.TestLoader().loadTestsFromTestCase(CountdownTestCase)
    
    device_name = mobile_util.get_device_name()
    
    # # Put them in the list
    test_list = [homepage_tests, latest_tests, article_tests, optimized_template_tests, widget_tests, zip_recruiter_tests, countdown_tests] # add product_table for image comparation
    
    #test_list = [subscribe_tests]
    if TimeMachine == True:
        test_list.append(time_machine)
        print time_machine
    smoke_tests = unittest.TestSuite(test_list)
    
    env = env_util.get_env().upper()
    
    # # File
    sys.stdout.flush()
    dir = os.getcwd()
    #outfile = open(dir + "\RegressionTestReport.html", "w")
    outfile = open(dir + os.sep +device_name+"MobileSmokesReport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='BND Smokes Report - '+env, description=' Smokes Tests', \
                                            verbosity=2)
    sys.stdout.flush()
    runner.run(smoke_tests)

    
if __name__ == "__main__":
    device_name = mobile_util.get_device_name()
    TimeMachine = False
    if len(argv) > 3:
        TimeMachine = True
    #unittest.main(verbosity=2)            
    main(TimeMachine)
    mail(RESULTS_EMAIL,
    "BUSINESSNEWSDAILY - Mobile ("+device_name+") - Smoke Tests Report - "+env_util.get_env().upper(),
    "See attachment for the test results",
    device_name+"MobileSmokesReport.html")
    
