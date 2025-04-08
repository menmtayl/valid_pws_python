import re

password = input("Enter the Password:")
password_len = len(password)
forbidden_words = ["password", "123", "qwerty"]
is_valid = False

# Using infiinite while loop

while True: 
    if password_len <8 or password_len >16: break
    elif not re.search('[A-Z]', password): break
    elif not re.search('[0-9]', password): break
    elif not re.search('[$#@!]', password): break
    elif not re.search('.islower()', password): break
    elif not re.search('.isupper()',password): break
    elif re.search('\s', password): break
    elif re.search('pass', password): break
    elif re.search('qwerty', password): break
    elif re.search('123', password):break
    else:
        is_valid = True 
        break
        
if is_valid: 
    print("Password is valid.")
else: 
    print("Password is invalid.")