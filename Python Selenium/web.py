from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

#Define URL
main_url = 'https://twitter.com'
tab_url_1 = 'https://stackoverflow.com'
tab_url_2 = 'https://www.selenium.dev'
PATH = "C:\Program Files (x86)\chromedriver.exe"

#Start Chrome with first link
driver = webdriver.Chrome(PATH)
driver.maximize_window()
actions = ActionChains(driver)
driver.get(main_url)

#Tab 2
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[1])
driver.get(tab_url_1)

#Tab 3
driver.execute_script("window.open('');")
driver.switch_to_window(driver.window_handles[2])
driver.get(tab_url_2)

while True:
    time.sleep(10)
    Windows = driver.window_handles
    for window in Windows:
        driver.switch_to_window(window)
        driver.refresh()