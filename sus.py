import time
import random
import win32api, win32con, win32clipboard
from pynput.keyboard import Key, Controller
import keyboard as kboard

keyboard = Controller()

print('Started! hold the \'ctrl\' key to run script.')

while 1:

    while kboard.is_pressed('ctrl') == False:
    
        time.sleep(0.5)
        print('Started! hold the \'ctrl\' key to run script.')
    
    time.sleep(0.5)
    print('Starting!')
    time.sleep(0.1)

    while kboard.is_pressed('Esc') == False:

        print('Thinking...')
        time.sleep(random.uniform(0.2, 1.001))
        print('Finished thunk!')
        print('Begining processing, hold \'Esc\' to abort.')
        time.sleep(0.01)
    
        while 1:
        
            try:
            
                print('Trying to access the clipboard.')
                win32clipboard.OpenClipboard()
                break

            except Exception:
        
                print('Clipboard access failed :( , trying again in 0.1 seconds.')
                time.sleep(0.1)
                continue
        
        time.sleep(0.01)
        print('Reading clipboard.')
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        time.sleep(0.01)
        print('Typing...')
    
        for n in data:
        
            keyboard.type(n)
            time.sleep(random.uniform(0.0001, 0.1))
        
            if kboard.is_pressed('Esc'):
            
                print('manually aborted.')
                break
        
        time.sleep(random.uniform(0.2, 0.5))
        print('Finished typing or manually aborted. The answer was \'{}\'.'.format(data))
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
