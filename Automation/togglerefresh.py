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
    if keyboard.is_pressed('Ctrl+Shift+F3'):
        toggl = 'Close Program'
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Close Program",icon_path=None,duration=2)
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        break

    if keyboard.is_pressed('Ctrl+F3'):
        toggl = 'Stop Script'
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Stop Auto Refresh Script",icon_path=None,duration=2)

    if keyboard.is_pressed('Ctrl+F2'):
        toggl = 'Run Script'
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Run Auto Refresh Script",icon_path=None,duration=2)

    if toggl == 'Run Script':
        time.sleep(5)
        Windows = driver.window_handles
        for window in Windows:
            driver.switch_to_window(window)
            driver.refresh()