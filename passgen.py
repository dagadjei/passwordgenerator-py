import string
import random

def password_gen():
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    num = string.digits
    symbols = string.punctuation

    passlen = int(input("Enter Password Length: ")) 
    s = []
    s.extend(list(upper))
    s.extend(list(lower))
    s.extend(list(num))
    s.extend(list(symbols))
    random.shuffle(s)
    password = ("".join(s[0:passlen]))
    print(password)    

password_gen()   


