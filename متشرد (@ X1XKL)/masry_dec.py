# Decompiled BY : Sidra ELEzz 
# follw my tele : @SidraTools
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
x = n + '\n\n\n\n\t\t\t\t💣تشفير مصري🛰️\n\t\t\t\t\n\t\t\t\t\n\n\n '
combo(x)
print(o + '\n\x1b[39;1mDiv ==> @تشفير\n')
city = input(Fore.GREEN + '\tEnter the beginning of the numbers mr youssef  : ')
use = '07738840487'
many = input(Fore.YELLOW + '\n\tHow many numbers do you want mr تش ? : ')
many = int(many)
letter = input(Fore.BLUE + '\n\tHow many letters mr youssef ? : ')
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
            with open('tshfer.txt', 'a') as x:
                x.write(city + num + ':' + city + num + '\n')