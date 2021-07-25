# Decrypt By Sidra ELEzz
# Github : https://github.com/SidraELEzz
# Telegram: https://t.me/TT_RQ
#It is not good for your personality that everything in you is great except for your mind
import random, sys, time
from colorama import Fore
from time import sleep

def combo(s):
    for ASU in s + '\n':
        sys.stdout.write(ASU)
        sys.stdout.flush()
        sleep(0.006666666666666667)


n = '\x1b[1;35m'
j = '\x1b[1;36m'
o = '\x1b[1;31m'
x = n + '\n\n 𝗕𝗬 : @SidraTOOLS\n\t\t\t\t\n '
combo(x)
print(o + '\n\x1b[39;1mDiv ==> @E999G\n')
city = input(Fore.GREEN + '\tاختار بدايه الرقم؟ : ')
use = '1234567890'
many = input(Fore.YELLOW + '\n\tاختار عدد الرقام؟ : ')
many = int(many)
letter = input(Fore.BLUE + '\n\tاختار نهايه الرقام؟ : ')
letter = int(letter)
print(j + '')
for num in range(many):
    num = ''
    for item in range(letter):
        num = ''
    else:
        for item in range(letter):
            num += random.choice(use)
        else:
            print('\t' + city + num + ':' + city + num)
            with open('list.txt', 'a') as x:
                x.write(city + num + ':' + city + num + '\n')
