import random

length = int(input("Password Length : "))
if (length < 6):
    print('Please enter more than 6 in your next try'.upper())
    exit()
    
print('Enter 1 for TRUE and 0 for FALSE')

try :
    sym = bool(int(input('Allow Symbols (!@#$%^&*()+) : ')))
    num = bool(int(input('Allow Numbers (0-9) : ')))
    lc = bool(int(input('Allow Lowercase (abc) : ')))
    uc = bool(int(input('Allow Uppercase (ABC) : ')))
    dup = bool(int(input('Exclude Duplicate Charaters : ')))
    otherSym = bool(int(input('Allow Other Symbols (~`[];?,) : ')))
except Exception:
    print('''Please don't enter something else!!!!! \nJust enter ZERO for FALSE and ONE for TRUE :)''')
    exit()


symbols = ['!','@','#','$','%','^','*','&','(',')','+']
numbers = ['1','2','3','4','5','6','7','8','9','0']
lowercase = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
otherSymbols = ['~','`','[',']',';','?',',']


add = []


if (sym == True):
    add.extend(symbols)
if (num == True):
    add.extend(numbers)
if (lc == True):
    add.extend(lowercase)
if (uc == True):
    add.extend(uppercase)
if (otherSym == True):
    add.extend(otherSymbols)


if (dup == True):
    password = random.sample(add,length-1)
    password.extend(random.choice(password))
else : 
    password = random.sample(add,length)
 
print(''.join(password))


# a = bool(int(input()))
# print(a)
