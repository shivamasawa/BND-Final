import sys
import time
from appium.webdriver.common.touch_action import TouchAction


def get_desired_capabilities(device_name):
    desired_caps = {}
    if(device_name == "iphone"):
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['browserName'] = 'Safari'
        desired_caps['deviceName'] = 'iPhone 6'
        desired_caps['autoWebview'] = True
        desired_caps["automationName"] = 'XCUITest'
                    
    if(device_name == "ipad"):
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.3'
        desired_caps['browserName'] = 'Safari'
        desired_caps['deviceName'] = 'iPad Air 2'
        desired_caps['autoWebview'] = True
        desired_caps["automationName"] = 'XCUITest'
            
#    if(device_name.__contains__("android")):               
#        desired_caps['platformName'] = 'Android'
#        desired_caps['platformVersion'] = '7.1'
#        desired_caps['browserName'] = 'Chrome'
#        desired_caps['deviceName'] = 'Android Emulator'
        
    if(device_name.__contains__("android")):               
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1.1'
        desired_caps['browserName'] = 'Chrome'
        desired_caps['deviceName'] = 'Android Emulator'
    return desired_caps

def get_device_name():
    if len(sys.argv) == 3:
        device_name = sys.argv[2].lower()
    elif len(sys.argv) == 2:
        device_name = sys.argv[1].lower()
    else:
        device_name = "android_phone"
    return device_name

def tap_webview_element(driver, device_name, web_element):
    #based on: https://github.com/appium/appium/issues/3896
    
    #Gather information of webview
    #Webview dimentions
    screen_webview_width = int(driver.execute_script("return window.innerWidth || document.body.clientWidth"))
    screen_webview_height = int(driver.execute_script("return window.innerHeight || document.body.clientHeight"))
    #Element coordinates in webview
    element_webview_location = web_element.location
    size = web_element.size
    element_webview_center_x = int(element_webview_location.get('x') + (size.get('width') / 2))
    element_webview_center_y = int(element_webview_location.get('y') + (size.get('height') / 2))
    web_context = driver.context
    
    #Switching to native view
    driver.switch_to.context('NATIVE_APP')
    
    #Screen information
    screen_width = driver.get_window_size().get('width')
    screen_height = driver.get_window_size().get('height')
    service_url_bar = 69;
    if('tablet' in device_name):
        service_url_bar = 245;
    relative_screen_view_height = screen_height - service_url_bar
    
    element_native_view_x = int((element_webview_center_x * screen_width) / screen_webview_width)
    element_native_view_y = int((element_webview_center_y * relative_screen_view_height) / screen_webview_height)
    
    actions = TouchAction(driver)
    actions.tap(None, element_native_view_x,element_native_view_y+service_url_bar).perform()
    
    driver.switch_to.context(web_context)
    
def tap_webview_element_with_offset(driver, device_name, web_element, x_offset):
    #based on: https://github.com/appium/appium/issues/3896
    
    #Gather information of webview
    #Webview dimentions
    screen_webview_width = int(driver.execute_script("return window.innerWidth || document.body.clientWidth"))
    screen_webview_height = int(driver.execute_script("return window.innerHeight || document.body.clientHeight"))
    #Element coordinates in webview
    element_webview_location = web_element.location
    size = web_element.size
    element_webview_center_x = int(element_webview_location.get('x') + (size.get('width') / 2))+x_offset
    element_webview_center_y = int(element_webview_location.get('y') + (size.get('height') / 2))
    web_context = driver.context
    
    #Switching to native view
    driver.switch_to.context('NATIVE_APP')
    
    #Screen information
    screen_width = driver.get_window_size().get('width')
    screen_height = driver.get_window_size().get('height')
    service_url_bar = 69;
    if('tablet' in device_name):
        service_url_bar = 245;
    relative_screen_view_height = screen_height - service_url_bar
    
    element_native_view_x = int((element_webview_center_x * screen_width) / screen_webview_width)
    element_native_view_y = int((element_webview_center_y * relative_screen_view_height) / screen_webview_height)
    
    actions = TouchAction(driver)
    actions.tap(None, element_native_view_x,element_native_view_y+service_url_bar).perform()
    
    driver.switch_to.context(web_context)
    
def tap_coordinate(driver, x, y):
    web_context = driver.context
    #Switching to native view
    driver.switch_to.context('NATIVE_APP')
    actions = TouchAction(driver)
    actions.tap(None, x, y).perform()
    driver.switch_to.context(web_context)
    
def accept_chrome_welcome(driver, device_name):
    if device_name.__contains__('phone'):
        tap_coordinate(driver, 539, 1674)
        time.sleep(1)
        tap_coordinate(driver, 201, 1674)
    else:
        tap_coordinate(driver, 800, 1927)
        time.sleep(1)
        tap_coordinate(driver, 375, 1927)
        
def get_browser_width(device_name, driver):
    browser_width = 0
    if ('android' in device_name) or ('Android' in device_name):
        browser_width = driver.execute_script("return window.innerWidth")
    else:
        browser_size = driver.get_window_size()
        browser_width = browser_size.get('width')
    return browser_width

def get_platform_name(driver):
    return str(driver.desired_capabilities['platformName'])
    
    