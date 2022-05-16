from operator import is_not
import pyautogui as pag
method=input('read from (f)ile, spam (n)umbers or enter a (c)ustom msg? ')

def check_method(method):
    if method!='f' and method!='c' and method!='n':
        print('please, enter a correct method!')
        method=input('read from (f)ile, spam (n)umbers or enter a (c)ustom msg? ')
        check_method(method)
    else:
        pass

check_method(method)
number=int(input('how many times? '))

def sleep_timer():
    for i in range(5):
        print(f'starting after {5-i}s...')
        pag.sleep(1)

def spam_from_file(number):
    f=open('spamtext.txt','r')
    msg=f.read()
    for i in range(number):
        pag.typewrite(msg+'\n')
    f.close()

def spam_number(number):
    while number!=0:
        pag.typewrite(str(number)+'\n')
        number-=1

def spam_text(text, number):
    for i in range(number):
        pag.typewrite(text+'\n')

if method=='f':
    sleep_timer()
    spam_from_file(number)
elif method=='c':
    msg=input('enter your msg: ')
    sleep_timer()
    spam_text(msg, number)
elif method=='n':
    sleep_timer()
    spam_number(number)
