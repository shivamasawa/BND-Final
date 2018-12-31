from selenium.webdriver.common.action_chains import ActionChains

def hover(driver, elem):
    hov = ActionChains(driver).move_to_element(elem)
    hov.perform()      
    
def is_element_present(driver, css_selector):
    elements = driver.find_elements_by_css_selector(css_selector)
    if len(elements) < 1:
        return False
    else:
        return True
    
def is_element_displayed(driver, web_element):
    size = web_element.size
    width = size.get('width')
    height = size.get('height')
    if(width > 0 and height > 0):
        return True
    else:
        return False
    
def scroll_to_element(driver, elem):
    driver.execute_script("arguments[0].scrollIntoView();", elem)