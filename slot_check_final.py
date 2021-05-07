import re
import pyperclip as pp
import pyautogui
from datetime import datetime
from beepy import beep
import time

for j in range(32):
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

    time.sleep(35)

    if j == 1 or j == 11 or j == 21:
        pyautogui.click(100, 408)  # Continue: 100, 408

    elif j == 2 or j == 12 or j == 22:
        pyautogui.click(43, 340)  # Home: 43, 340

    elif j == 3 or j == 13 or j == 23:
        pyautogui.click(100, 408)  # Continue: 100, 408

    elif j == 4 or j == 14 or j == 24:
        pyautogui.click(43, 340)  # Home: 43, 340

    elif j == 5 or j == 15 or j == 25:
        pyautogui.click(132, 522)  # Provide Feedback: 132, 522

    elif j == 6 or j == 16 or j == 26:
        pyautogui.click(43, 340)  # Home: 43, 340

    elif j == 7 or j == 17 or j == 27:
        pyautogui.click(134, 488)  # Group Scheduling Request: 134, 488

    elif j == 8 or j == 18 or j == 28:
        pyautogui.click(43, 340)  # Home: 43, 340

    elif j == 9 or j == 19 or j == 29:
        pyautogui.click(153, 553)  # Update Profile: 153, 553

    elif j == 0 or j == 10 or j == 30:
        pyautogui.click(43, 340)  # Home: 43, 340

    elif j == 31:
        pyautogui.click(83, 583)  # Logout: 83, 583

    time.sleep(25)
