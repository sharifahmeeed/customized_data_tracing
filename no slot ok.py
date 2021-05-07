import re
import pyperclip as pp
import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# text =pp.paste()
#
# urls = re.findall('Continue', text)
#
# now = datetime.now()
#
# current_time = now.strftime("%H:%M:%S")
# print("Current Time =", text+','+current_time)


#text ="gaggagga ggagga First Available Appointment Is Thursday January 021."

text =pp.paste()
nameRegex = re.compile(r'\w* +\d\d+\W+\d\d\d\d+\W')
mo = nameRegex.search(text)


#urls = re.findall('Continue', text)

now = datetime.now()


current_time = now.strftime("%H:%M:%S")

if mo:
    print(mo.group() +' and '+current_time)
else:
    print("No Slot and "+current_time)