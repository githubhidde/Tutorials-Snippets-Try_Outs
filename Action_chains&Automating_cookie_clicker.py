# Here you automate the cookieclicker game from: https://orteil.dashnet.org/cookieclicker

# First things first!
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "D:\Python\Extensions\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# cookieclicker
driver.get("https://orteil.dashnet.org/cookieclicker")

driver.implicitly_wait(5)

# Find the big cookie
cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

items = [driver.find_element_by_id("productPrice" + str(i)) for i in range (1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

# This represents how many times you want to click the cookie
for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    
# buy immediately items on the right pane if possible
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()



