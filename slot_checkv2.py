import re
import pyperclip as pp
import pyautogui
from datetime import datetime
from beepy import beep
import time

## customization thread start# for my samsumg pc

cgi_blank_click1 = 133
cgi_blank_click2 = 924
cgi_blank_click3 = 350
cgi_blank_click4 = 924
msg_init_click1 = 1521
msg_init_click2 = 1044

con_1 = 100
con_2 = 408
hom_1 = 43
hom_2 = 340
fed_1 = 132
fed_2 = 522
sch_1 = 134
sch_2 = 468
upd_1 = 153
upd_2 = 553
log_1 = 83
log_2 = 583

# customization thread end


def human_behavior(con1, con2, hom1, hom2, fed1, fed2, sch1, sch2, upd1, upd2, log1, log2):
    if j in [1, 11, 21]:
        pyautogui.click(con1, con2)  # Continue: 100, 408

    elif j % 2 == 0:
        pyautogui.click(hom1, hom2)  # Home: 43, 340

    elif j in [3, 13, 23]:
        pyautogui.click(con1, con2)  # Continue: 100, 408

    elif j % 5 == 0:
        pyautogui.click(fed1, fed2)  # Provide Feedback: 132, 522

    elif j in [7, 17, 27]:
        pyautogui.click(sch1, sch2)  # Group Scheduling Request: 134, 488

    elif j in [9, 19, 29]:
        pyautogui.click(upd1, upd2)  # Update Profile: 153, 553

    elif j == 31:
        pyautogui.click(log1, log2)  # Logout: 83, 583


def alarm_msg_call():
    for i in range(3):
        print(" Please Book Slot! Slot Open For " + mo.group()[0:3])
        pp.copy(" Please Book Slot! Slot Open For " + mo.group()[0:3])

    for i in range(7):
        beep(sound=2)  # integer as argument
        beep(sound='coin')  # string as argument
        beep(sound=2)  # integer as argument
        beep(sound='coin')  # string as argument

    # pyautogui.click(1743, 228)  #call messenger group

# code for half hour
for j in range(32):

    reloadCheck = None

    while not reloadCheck:
        reloadCheck = pyautogui.locateOnScreen('reload_complete.PNG')
        if reloadCheck:
            # pyautogui.moveTo(400, 800)
            pyautogui.click(cgi_blank_click1, cgi_blank_click2)  # (133, 924)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey('ctrl', 'c')
            pyautogui.click(cgi_blank_click3, cgi_blank_click4)  # (350, 924)

            # text ="gaggagga ggagga First Available Appointment Is Thursday January 021."

            text = pp.paste()

            nameLoginCheck = re.compile(r'Logged in as ')
            login_check = nameLoginCheck.search(text)

            nameRegex = re.compile(r'\w* +\d\d+\W+\d\d\d\d+\W')
            mo = nameRegex.search(text)

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            pyautogui.click(msg_init_click1, msg_init_click2)  # click for message (1521, 1044)

            if (login_check):
                if (mo):
                    print(mo.group() + ' and ' + current_time)
                    pp.copy(mo.group() + ' and ' + current_time)

                    if ((mo.group()[0:3] == "May") | (mo.group()[0:3] == "Jun") | (mo.group()[0:3] == "Jul") | (
                            mo.group()[0:3] == "Aug")):

                        alarm_msg_call()  # when system generates alarm and mgs

                else:
                    print("No Slot and " + current_time)
                    pp.copy("No Slot and " + current_time)

            else:
                print("Not logged in")
                pp.copy("Not logged in")
                beep(sound='coin')  # string as argument
                beep(sound='coin')  # string as argument

            if len(pp.paste() < 100):  # to skip full copy site copy paste problem
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.hotkey('enter')

            else:
                pp.copy("Sorry! Data Error")
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.hotkey('enter')

    time.sleep(53)

    # human_behavior(con1, con2, hom1, hom2, fed1, fed2, sch1, sch2, upd1, upd2, log1, log2)
    human_behavior(con_1, con_2, hom_1, hom_2, fed_1, fed_2, sch_1, sch_2, upd_1, upd_2, log_1, log_2)
