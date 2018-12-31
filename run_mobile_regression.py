import unittest
import utils.mobile_util as mobile_util
from tests.mobile_test_homepage import HomepageTestCase
from tests.mobile_test_subscribe  import SubscribeTestCase
from tests.mobile_test_latest import LatestTestCase
from tests.mobile_test_article import ArticleTestCase
from tests.mobile_test_404 import F04TestCase
from tests.mobile_test_credits import CreditsTestCase
#from img_comp_productable import ProductTableTest
from tests.mobile_test_businessideagenerator import BIGTestCase
from tests.mobile_test_quiz import QuizCase
from tests.mobile_time_machine import TimeMachineTest
from tests.mobile_test_header_search import HeaderSearchTestCase
from tests.mobile_layout_test import MobileLayoutTestCase
from tests.tablet_layout_test import TabletLayoutTestCase
from tests.mobile_test_optimized_template import OptimizedTemplateTestCase
from tests.tablet_test_subheader_nav import TabletSubheaderTestCase
from tests.mobile_test_search import SearchTestCase;
from tests.mobile_test_widget_loads import WidgetTestCase
#from tests.mobile_test_offer_logic import OfferLogicTestCase
from tests.mobile_test_about_us import AboutUsTestCase

import utils.HTMLTestRunner as HTMLTestRunner
from utils.email_sender import mail
import tests.mobile_time_machine as mobile_time_machine
import os
from sys import argv
import sys
from configs.config import RESULTS_EMAIL

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
    mobile_layout_tests = unittest.TestLoader().loadTestsFromTestCase(MobileLayoutTestCase)
    tablet_layout_tests = unittest.TestLoader().loadTestsFromTestCase(TabletLayoutTestCase)
    optimized_layout_tests = unittest.TestLoader().loadTestsFromTestCase(OptimizedTemplateTestCase)
    tablet_subheader_tests = unittest.TestLoader().loadTestsFromTestCase(TabletSubheaderTestCase)
    search_tests = unittest.TestLoader().loadTestsFromTestCase(SearchTestCase)
    widget_tests = unittest.TestLoader().loadTestsFromTestCase(WidgetTestCase)
    #offer_logic_tests = unittest.TestLoader().loadTestsFromTestCase(OfferLogicTestCase)
    about_us_tests = unittest.TestLoader().loadTestsFromTestCase(AboutUsTestCase)
    
    layout_tests = None
    device_name = mobile_util.get_device_name()
    if(device_name.__contains__('phone')):
        layout_tests = mobile_layout_tests
        test_list = [homepage_tests, latest_tests, article_tests, \
                                      f04_tests, credits_tests, big_tests, quiz_test, header_search_tests, 
                                      layout_tests, optimized_layout_tests, search_tests, 
                                      widget_tests, about_us_tests] # add product_table for image comparation
    else:
        layout_tests = tablet_layout_tests
        # # Put them in the list
        test_list = [homepage_tests, latest_tests, article_tests, \
                                      f04_tests, credits_tests, big_tests, quiz_test, header_search_tests, 
                                      layout_tests, optimized_layout_tests, tablet_subheader_tests, 
                                      search_tests, widget_tests, about_us_tests] # add product_table for image comparation
    
    #test_list = [subscribe_tests]
    if TimeMachine == True:
        test_list.append(time_machine)
        print time_machine
    smoke_tests = unittest.TestSuite(test_list)
    
    
    # # File
    sys.stdout.flush()
    dir = os.getcwd()
    #outfile = open(dir + "\RegressionTestReport.html", "w")
    report_name = device_name+"RegressionTestReport.html"
    outfile = open(dir + os.sep + report_name, "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='BND test Report - '+device_name, description=' Mobile Regression Tests', \
                                            verbosity=2)
    sys.stdout.flush()
    runner.run(smoke_tests)

    
if __name__ == "__main__":
    TimeMachine = False
    device_name = mobile_util.get_device_name()        
    main(TimeMachine)
    mail(RESULTS_EMAIL,
   "BUSINESSNEWSDAILY - Mobile ("+device_name+") Regression Test Report",
   "See attachment for the test results",
   device_name+"RegressionTestReport.html")
    
