import pyautogui
import pyperclip as pp
import time


while(1):
    time.sleep(1)
    print(pyautogui.position(), pyautogui.size())
    text ="Thursday January21."

    pp.copy(text)
    if(len(pp.paste())<80):
        print(pp.paste())
