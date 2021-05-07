import re
import pyperclip as pp
import pyautogui
from datetime import datetime
from beepy import beep
import time

for j in range(32):

    reloadCheck = None

    while not reloadCheck:
        reloadCheck = pyautogui.locateOnScreen('reload_complete.PNG')
        if reloadCheck:
            # pyautogui.moveTo(400, 800)
            pyautogui.click(133, 924)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.click(350, 924)

            # text ="gaggagga ggagga First Available Appointment Is Thursday January 021."

            text = pp.paste()

            nameLoginCheck = re.compile(r'Logged in as ')
            login_check = nameLoginCheck.search(text)

            nameRegex = re.compile(r'\w* +\d\d+\W+\d\d\d\d+\W')
            mo = nameRegex.search(text)

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            pyautogui.click(1521, 1044)

            if (login_check):
                if (mo):
                    print(mo.group() + ' and ' + current_time)
                    pp.copy(mo.group() + ' and ' + current_time)

                    if ((mo.group()[0:3] == "May") | (mo.group()[0:3] == "Jun") | (mo.group()[0:3] == "Jul") | (
                            mo.group()[0:3] == "Aug")):
                        for i in range(7):
                            beep(sound=2)  # integer as argument
                            beep(sound='coin')  # string as argument
                            beep(sound=2)  # integer as argument
                            beep(sound='coin')  # string as argument

                        for i in range(3):
                            print(" Please Book Slot! Slot Open For " + mo.group()[0:3])
                            pp.copy(" Please Book Slot! Slot Open For " + mo.group()[0:3])

                        pyautogui.click(1743, 228)  #call messenger group


                else:
                    print("No Slot and " + current_time)
                    pp.copy("No Slot and " + current_time)

            else:
                print("Not logged in")
                pp.copy("Not logged in")
                beep(sound='coin')  # string as argument
                beep(sound='coin')  # string as argument

            pyautogui.hotkey('ctrl', 'v')
            pyautogui.hotkey('enter')

    time.sleep(53)

    if j in [1, 11, 21]:
        pyautogui.click(100, 408)  # Continue: 100, 408

    elif j % 2 == 0:
        pyautogui.click(43, 340)  # Home: 43, 340

    elif j in [3, 13, 23]:
        pyautogui.click(100, 408)  # Continue: 100, 408

    elif j % 5 == 0:
        pyautogui.click(132, 522)  # Provide Feedback: 132, 522

    elif j in [7, 17, 27]:
        pyautogui.click(134, 488)  # Group Scheduling Request: 134, 488

    elif j in [9, 19, 29]:
        pyautogui.click(153, 553)  # Update Profile: 153, 553

    elif j == 31:
        pyautogui.click(83, 583)  # Logout: 83, 583


