import unittest
from tests.test_homepage import HomepageTestCase
from tests.test_subscribe  import SubscribeTestCase
from tests.test_latest import LatestTestCase
from tests.test_article import ArticleTestCase
from tests.test_404 import F04TestCase
from tests.test_credits import CreditsTestCase
#from img_comp_productable import ProductTableTest
from tests.test_businessideagenerator import BIGTestCase
from tests.test_quiz import QuizCase
from tests.time_machine import TimeMachineTest
from tests.test_header_search import HeaderSearchTestCase
from tests.test_optimized_template import OptimizedTemplateTestCase
from tests.test_subheader_nav import SubheaderTestCase
from tests.test_search import SearchTestCase
from tests.test_widget_loads import WidgetTestCase
from tests.test_offer_logic import OfferLogicTestCase
from tests.test_countdown import CountdownTestCase
from tests.test_about_us import AboutUsTestCase

import utils.HTMLTestRunner as HTMLTestRunner
from utils.email_sender import mail
import tests.time_machine as time_machine
import os
from sys import argv
import sys
from configs.config import RESULTS_EMAIL
import utils.env_util as env_util

# run the nosetests img_comp_productable.py --with-save-baseline for the baseline images


def main(TimeMachine):
    
    time_machine = unittest.TestLoader().loadTestsFromTestCase(TimeMachineTest)
    homepage_tests = unittest.TestLoader().loadTestsFromTestCase(HomepageTestCase)
    latest_tests = unittest.TestLoader().loadTestsFromTestCase(LatestTestCase)
    article_tests = unittest.TestLoader().loadTestsFromTestCase(ArticleTestCase)
    f04_tests = unittest.TestLoader().loadTestsFromTestCase(F04TestCase)
    credits_tests = unittest.TestLoader().loadTestsFromTestCase(CreditsTestCase)
    #product_table = unittest.TestLoader().loadTestsFromTestCase(ProductTableTest)
    big_tests = unittest.TestLoader().loadTestsFromTestCase(BIGTestCase)
    quiz_test = unittest.TestLoader().loadTestsFromTestCase(QuizCase)
    header_search_tests = unittest.TestLoader().loadTestsFromTestCase(HeaderSearchTestCase)
    optimized_template_tests = unittest.TestLoader().loadTestsFromTestCase(OptimizedTemplateTestCase)
    sub_header_tests = unittest.TestLoader().loadTestsFromTestCase(SubheaderTestCase)
    search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTestCase)
    widget_tests = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    offer_logic_tests = unittest.TestLoader().loadTestsFromTestCase(OfferLogicTestCase)
    countdown_tests = unittest.TestLoader().loadTestsFromTestCase(CountdownTestCase)
    about_us_tests = unittest.TestLoader().loadTestsFromTestCase(AboutUsTestCase)
    
    # # Put them in the list
    test_list = [homepage_tests, latest_tests, article_tests, \
                                      f04_tests, credits_tests, big_tests, quiz_test, header_search_tests, optimized_template_tests, 
                                      sub_header_tests, search_tests, widget_tests, offer_logic_tests, countdown_tests, about_us_tests] # add product_table for image comparation
    
    #test_list = [subscribe_tests]
    if TimeMachine == True:
        test_list.append(time_machine)
        print time_machine
    smoke_tests = unittest.TestSuite(test_list)
    
    env = env_util.get_env().upper()
    browser = env_util.get_browser()
    
    # # File
    sys.stdout.flush()
    dir = os.getcwd()
    #outfile = open(dir + "\RegressionTestReport.html", "w")
    outfile = open(dir + os.sep +browser+"RegressionTestReport.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='BND Regression Report - '+env+' - '+browser, description=' Regression Tests', \
                                            verbosity=2)
    sys.stdout.flush()
    runner.run(smoke_tests)

    
if __name__ == "__main__":
    TimeMachine = False
    if len(argv) > 3:
        TimeMachine = True
    #unittest.main(verbosity=2)            
    main(TimeMachine)
    browser=env_util.get_browser()
    '''mail(RESULTS_EMAIL,
   "BUSINESSNEWSDAILY - Regression Test Report - "+env_util.get_env().upper()+" - "+browser,
   "See attachment for the test results for the "+browser+" browser",
   browser+"RegressionTestReport.html")'''
    
