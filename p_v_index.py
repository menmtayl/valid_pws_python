# password_validation
# Password Rule Statement 

# Password outputs 
# Contains 8-12 Character
# contains one special character
# contains atleast on number
# contains at least on capital letter

# def valid_password(password) rules

def valid_password(password):
   if (len(password) <8): 
        return False
    
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False 
    
# loop for validation: 
symbols = "!\#%''()*+,-/:;<=>>@[\]"

for character in password: 
    
    if character.islower(): 
        has_lower=True
        
    if character.isupper(): 
        has_upper = True 
        
    if character is digit():
        has_digit = True
    
    if character in symbols: 
        has_symbol = True
        
return has_lower and has upper and \
       has_digit and has has_symbol
    
valid_password("gum4all#")
