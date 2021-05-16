import re
import pyperclip as pp
import pyautogui
from datetime import datetime
from beepy import beep
import time

## customization thread start#



cgi_blank_click1 = 133
cgi_blank_click2 = 924
cgi_blank_click3 = 350
cgi_blank_click4 = 924


msg_init_click1 = 1521
msg_init_click2 = 1044
msg_call1 = 1749
msg_call2 = 223

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
while 1:
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    current_month = now.strftime("%b")

    pp.copy(" NNS " + current_time + current_month)

    print( NNS 21:14May)
    # pyautogui.click(msg_init_click1, msg_init_click2)
    # pyautogui.hotkey('ctrl', 'v')
    # pyautogui.hotkey('enter')

    time.sleep(5)
