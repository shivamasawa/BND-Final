def verifyAdLoadsAndClose(driver):
    driver = driver;
    try:
        ads2 = driver.find_elements_by_css_selector("div[id*='_lb_close']")
        if(len(ads2) > 0):
            ads2[0].click()
        else:
            elem = driver.find_element_by_css_selector("div[id*='bom_footer_closed_state']")
            elem.find_element_by_id("close_area_1").click()
    except Exception:
        print("Ad was not displayed")