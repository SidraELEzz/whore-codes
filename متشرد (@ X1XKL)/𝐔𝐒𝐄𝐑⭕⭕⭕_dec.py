# Decompiled BY : Sidra ELEzz 
# follw my tele : @SidraTools
import time, requests, webbrowser, sys as n, random, webbrowser, threading
rhaby2 = int(5)
rhaby = int(1)
ruksI = 'IdMN1w9spls'
rg = 'D'
ruks_ = '\x1b[1;36m'
ruks__ = '\x1b[1;36m'
jruks = '\x1b[1;37m'
_ruks = '\x1b[1;31m'
BGreen = '\x1b[1;32m'
BRed = '\x1b[1;31m'
N = 0
R = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'
print(f"{BGreen}{R}\n──────▄▄▄▄▄███████████████████▄▄▄▄▄──────\n────▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄────\n──▄██▀████████▄─────────────▀▀████─▀██▄──\n─▀██▄▄██████████████████▄▄▄─────────▄██▀─\n───▀█████████████████████████▄────▄██▀───\n─────▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀─────\n───────▀███▄──────────────▀██████▀───────\n─────────▀██████▄─────────▄████▀─────────\n────────────▀█████▄▄▄▄▄▄▄███▀────────────\n──────────────▀████▀▀▀████▀──────────────\n────────────────▀███▄███▀────────────────\n───────────────────▀█▀───────────────────\n█▀▄▀█ █▀▀█ █░░█ █▀▀█ █▀▀ █▀▄▀█ █▀▀█ █▀▀▄\n█░▀░█ █░░█ █▀▀█ █▄▄█ █▀▀ █░▀░█ █▄▄█ █░░█\n▀░░░▀ ▀▀▀▀ ▀░░▀ ▀░░▀ ▀▀▀ ▀░░░▀ ▀░░▀ ▀░░▀\n\n{R}\n")
rukS = input(jruks + '[' + _ruks + '+' + jruks + ']' + ruks__ + ' TOKEN ! -> :' + BGreen)
Ruks = input(jruks + '[' + _ruks + '+' + jruks + ']' + ruks__ + ' ID ! -> :' + BGreen)
print(R)

def ruks():
    global N
    global Ruks
    global rukS
    tuks1 = 'poiuytrewqasdfghjklmnbvcxz1234567890'
    t = 'poiuytrewqasdfghjklmnbvcxz1234567890'
    ruKs = requests.session()
    try:
        while True:
            N += 1
            rhaby1 = str(''.join((random.choice(t) for i in range(2))))
            email = str(''.join((random.choice(tuks1) for i in range(1))))
            for password in range(rhaby):
                password = ''
                for item in range(rhaby2):
                    rhaby3 = ''
                else:
                    for item in range(rhaby2):
                        rhaby3 += random.choice(rhaby1)
                    else:
                        user = rhaby3 + email
                        url = f"https://t.me/{user}"
                        req = ruKs.get(url)
                        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
                            print(jruks + '[' + BGreen + (f"{N}") + jruks + '] Available' + BGreen + f" [{user}]")
                            RUKS3 = f"https://api.telegram.org/bot{rukS}/sendMessage?chat_id={Ruks}&text=𓆩✅ تم الصيد  يوزر 𓆪✥\n𝖷𝗑----------𝗑---------------𝗑-------𝗑𝖷𝖷𝗑----------𝗑---\n✥. 🇮🇶𝐔𝐒𝐄𝐑 : @{user} \n𝖷𝗑----------𝗑---------------𝗑---------𝗑𝖷𝖷𝗑----------𝗑-\n𓆩72𓆪قـٰ̲ـہيـٰ̲ـہاٰدٰيـٰ̲ـہ : 𝐓𝐞𝐥𝐞 : @X1XKL : @ee2_i"
                            req = ruKs.post(RUKS3)
                        else:
                            print(jruks + '[' + BRed + (f"{N}") + jruks + '] Unavailable' + BRed + f"-[{user}]")

    except:
        print(' 𝐓𝐞𝐥����: X1XKLR☆ : @X1XKL ')


thread = []
for i in range(100):
    thread1 = threading.Thread(target=ruks)
    thread1.start()
    thread.append(thread1)
else:
    for thread2 in thread:
        thread2.join