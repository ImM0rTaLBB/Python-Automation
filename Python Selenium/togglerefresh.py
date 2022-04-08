import keyboard
import time
from win10toast import ToastNotifier
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Define
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
toggl = 0

#Create Loop for Toggling Script
while True:
    print(toggl)

    if keyboard.is_pressed('q'):
        toggl = 0
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Close Program",icon_path=None,duration=2)
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        break

    if keyboard.is_pressed('f'):
        toggl = 1
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Stop Auto Refresh Script",icon_path=None,duration=2)

    if keyboard.is_pressed('d'):
        toggl = 2
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Run Auto Refresh Script",icon_path=None,duration=2)

    if toggl == 2:
        time.sleep(5)
        Windows = driver.window_handles
        for window in Windows:
            driver.switch_to_window(window)
            driver.refresh()