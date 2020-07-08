import random
import string
import time

def passwordgen(password, host, chares):
        chars0 = string.ascii_letters# + string.digits + "@$*!?/"
        chars1 = string.ascii_letters + string.digits# + "@$*!?/"
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
        start = time.time()
        tries = 0
        print(start)
        while cycle == True:
                password=''
                brutePass = passwordgen(password, host, chares)
                if brutePass not in DeniedPass:
                        if brutePass == host:
                                end = time.time()
                                print('*****Succesfully hacked*****\n* Password is ', brutePass ,' *\n* Time lost : ',end - start,' *\n* tries to hack: ', tries ,' *')
                                cycle = False
                        else:
                                print(brutePass, ' not password\n')
                                tries += 1
                                DeniedPass.append(brutePass)

host = input('Input password to check:  ')
bruteforce(host)
exits = input('\n\nPress Enter..')