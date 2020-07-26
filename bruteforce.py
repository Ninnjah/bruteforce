import random
import string
from time import time
from os import system

def passwordgen(password, host, chares):
        chars0 = string.ascii_letters
        chars1 = string.ascii_letters + string.digits
        chars2 = string.ascii_letters + string.digits + "@$*!?/"
        i = 0
        charsn = ''
        if chares == 0:
                charsn = chars0
        elif chares == 1:
                charsn = chars1
        else:
                charsn = chars2
        while i < len(host):
                password = password + random.choice(charsn)
                i += 1
        return password

def bruteforce(host):
        print('*****Bruteforce is Start*****\n')
        DeniedPass = []
        cycle = True
        chares = int(input('* Brute only letter[0], letters and digits[1], letters, digits and symbols[2] *\n'))
        start = time()
        tries = 0
        while cycle == True:
                password=''
                brutePass = passwordgen(password, host, chares)
                if brutePass not in DeniedPass:
                        if brutePass == host:
                                end = time()
                                print('\n*****Succesfully hacked*****')
                                print('* Password is {} *'.format(brutePass))
                                print('* Time lost : {} secs *'.format(round(end - start)))
                                print('* tries to hack: {} *\a\a'.format(tries))
                                cycle = False
                                DeniedPass = None
                        else:
                                print('{} not password. tries: {}'.format(brutePass, tries), end='\r')
                                tries += 1
                                DeniedPass.append(brutePass)

# Clear the console // Очистка консоли
system('cls||clear')  
host = input('Input password to check:  ')
bruteforce(host)
exits = input('\n\nPress Enter..')