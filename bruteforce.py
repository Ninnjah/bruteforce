import random
import string
from time import time, sleep
import os

def main():
        # Clear the console // Очистка консоли
        os.system('cls||clear')
        host = input('Input password to check:  ')
        print('Select mode: ')
        print(' [0] Password gen\n',
                '[1] Password list\n',
                '-' * 16)
        cmd = input()
        if cmd == '0':
                start = time()
                bruteforce(host)
        if cmd == '1':
                start = time()
                brutelist(host, start)
        if cmd == 'exit':
                quit()
        else:
                print('Invalid command..')
                sleep(1)
                main()

# Password generation // Генерация пароля
def passwordgen(password, host, chares):
        chars0 = string.ascii_letters
        chars1 = string.ascii_letters + string.digits
        chars2 = string.ascii_letters + string.digits + "@$*!?/"
        i = 0
        charsn = ''
        start = None
        start = time()
        while True:
                if chares == 0:
                        charsn = chars0
                elif chares == 1:
                        charsn = chars1
                else:
                        charsn = chars2
                while i < len(host):
                        password = password + random.choice(charsn)
                        i += 1
                if i == host:
                        # Clear the console // Очистка консоли
                        os.system('cls||clear')
                        print('\n*****Succesfully hacked*****')
                        print('* Password is {} *'.format(i))
                        print('* Time lost : {:.2f} secs *\a\a'.format(time() - start))
                        break
                else:
                        print('{} not password.                 '.format(i), end='\r')
        input()

# Чтение паролей из файла
def passwordlist(brutelist):
        with open(brutelist + '.txt', 'r', encoding='utf-8', errors='ignore') as f:   
            passwords = f.readlines()                   # Записываем каждую строку файла в список
        passwords = [x.strip() for x in passwords]      # Удаляем служебные символы
        return passwords

# Compare passwords // Сравнение паролей
def bruteforce(host, start):
        # Clear the console // Очистка консоли
        os.system('cls||clear')
        print('*****Bruteforce is Start*****\n')
        DeniedPass = []
        cycle = True
        chares = int(input('* Brute only letter[0], letters and digits[1], letters, digits and symbols[2] *\n'))
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

# Compare passwords // Сравнение паролей
def brutelist(host, start):
        # Clear the console // Очистка консоли
        os.system('cls||clear')
        brutelist = input('Enter brutelist".txt" name: ')
        if os.path.exists(brutelist + '.txt'):
                passwords = passwordlist(brutelist)
        else:
                print('didn found any files')
                sleep(1)
                brutelist(host, time())
        for i in passwords:
                if i == host:
                        end = time()
                        # Clear the console // Очистка консоли
                        os.system('cls||clear')
                        print('\n*****Succesfully hacked*****')
                        print('* Password is {} *'.format(i))
                        print('* Time lost : {:.2f} secs *\a\a'.format(end - start))
                        passwords = None
                        break
                else:
                        print('{} not password.                 '.format(i), end='\r')
                        passwords = None
        print('!!Password not in password list!!')
        input('\nPress Enter...')
        main()


if __name__ == '__main__':
        # Clear the console // Очистка консоли
        os.system('cls||clear')
        main()
