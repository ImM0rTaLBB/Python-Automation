import keyboard
import time
from win10toast import ToastNotifier

import pynput
from pynput.keyboard import Key, Controller

keyput = Controller()
toggl = 0

print('======================= Auto Refresh Script Software =======================')
print('This is the script software to auto press F5 every 5 second.')
print('Created By: AJI\n')
print('INSTRUCTION:')
print('Press F2 to Start Script.')
print('Press F3 to Stop Script (Hold F3 until notification shows up).')
print('Press F4 to Close Script Program.') 
print('This will also close an applcation that is on focus.') 
print('To avoid that, click on desktop first then press F4 to get out of focus).')
print('============================================================================\n')
print(':: STATUS ::')

while True:
    if keyboard.is_pressed('F4'):
        toggl = 'Close Program'
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Close Program",icon_path=None,duration=2)
        break

    if keyboard.is_pressed('F2'):
        toggl = 'Start Script'
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Run Auto Refresh Script",icon_path=None,duration=2)

    if keyboard.is_pressed('F3'):
        toggl = 'Stop Script'
        print(toggl)
        toaster = ToastNotifier()
        toaster.show_toast("Notification", "Stop Auto Refresh Script",icon_path=None,duration=2)

    if toggl == 'Start Script':
        time.sleep(5)
        keyput.press(Key.f5)
        keyput.release(Key.f5)