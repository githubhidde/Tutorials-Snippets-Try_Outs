# A depcrecated way of using PhantomJS

from selenium import webdriver
from phantomjs import Phantom
driver = webdriver.PhantomJS()
# driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
print("Open the below URL in your browser:")
print(driver.current_url)
driver.quit()

# Here you use Firefox to do some headless testing
# from selenium import webdriver
# driver = webdriver.Firefox()
# driver.get("https://duckduckgo.com/")
# driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
# driver.find_element_by_id("search_button_homepage").click()
# driver.quit()

