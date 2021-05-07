import re
import pyperclip as pp
import pyautogui
from datetime import datetime
from beepy import beep
import time



for j in range(30):
    #pyautogui.moveTo(400, 800)
    pyautogui.click(133, 924)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(350, 924)

    #text ="gaggagga ggagga First Available Appointment Is Thursday January 021."

    text =pp.paste()


    nameLoginCheck = re.compile(r'Logged in as ')
    login_check = nameLoginCheck.search(text)


    nameRegex = re.compile(r'\w* +\d\d+\W+\d\d\d\d+\W')
    mo = nameRegex.search(text)


    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


    pyautogui.click(1521, 1044)

    if (login_check):
        if (mo):
            print(mo.group() +' and '+current_time)
            pp.copy(mo.group() +' and '+current_time)

            if ( (mo.group()[0:3] == "May") | (mo.group()[0:3] == "Jun") | (mo.group()[0:3] == "Jul") | (mo.group()[0:3] == "Aug")  ):
                for i in range(3):
                    print(" Please Book Slot! Slot Open For " + mo.group()[0:3] )
                for i in range(5):
                    beep(sound=2)  # integer as argument
                    beep(sound='coin')  # string as argument
                    beep(sound=2)  # integer as argument
                    beep(sound='coin')  # string as argument


        else :
            print("No Slot and "+current_time)
            pp.copy("No Slot and "+current_time)

    else:
        print("Not logged in")
        pp.copy("Not logged in")



    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('enter')

    time.sleep(60)