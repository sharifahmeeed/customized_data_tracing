import pyautogui
import time

import beepy
from beepy import beep


time.sleep(2)


while(1):

        if(not(pyautogui.locateOnScreen('courses.PNG'))):
            beep(sound=2)  # integer as argument
            beep(sound='coin')  # string as argument
            beep(sound=2)  # integer as argument
            beep(sound='coin')  # string as argument