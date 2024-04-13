from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

##>.google-auth-button>> aria-labelledby="picker-item-label-0">>.input.search-global-typeahead__input>select all elements with ember-view class>try to click the first>

driver.get("https://www.linkedin.com")

google_auth_button = driver.find_element(By.CLASS_NAME, value="google-auth-button__placeholder")
google_auth_button.click()

################in order to swap to front page: 

# driver.window_handles
# New windows that have popped out from the base_window are further down in the sequence e.g.

# fb_login_window = driver.window_handles[1]
# We can switch our Selenium to target the new facebook login window by:

# driver.switch_to.window(fb_login_window)
# You can print the driver.title to verify that it's the facebook login window that is currently target:

# print(driver.title)
# The full code to switch to the new pop-up window is thus:

# base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(fb_login_window)
# print(driver.title)