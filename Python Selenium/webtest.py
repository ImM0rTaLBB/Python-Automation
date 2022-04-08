from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://developers.google.com/web/updates/2017/04/headless-chrome")
print(driver.title)

actions = ActionChains(driver)

for i in range(2880):
    time.sleep(5)
    driver.refresh()