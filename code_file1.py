import re

def validate_password(password):
    
    violated_rules = []

    
    if not 8 <= len(password) <= 16: # check password length
        violated_rules.append("Contains 8-16 characters")

    
    if not re.search(r"[%$#^&*!@()]", password): # check special charecters
        violated_rules.append("Contains one of the special characters: %$#^&*!@()")

    
    if not re.search(r"\d", password): # check at least on number
        violated_rules.append("Contains at least one number 0-9")

    
    if not re.search(r"[A-Z]", password): # check capital numbers
        violated_rules.append("Contains at least one capital letter")

    
    if not password[0].islower(): # check start with lower case
        violated_rules.append("Starts with a lowercase letter")

   
    restricted_phrases = ["pass", "qwerty", "123"] # check restricted phrases
    for phrase in restricted_phrases:
        if phrase in password:
            violated_rules.append(f"Must not contain the phrase '{phrase}'")

    return violated_rules if violated_rules else None

def main(): # define dunder methode
    
    print("ENTER THE PASSWORD USING FOLLOWING RULE:")
    print("- Contains 8-16 characters")
    print("- Contains one of the special characters: %$#^&*!@()")
    print("- Contains at least one number 0-9")
    print("- Contains at least one capital letter")
    print("- Starts with a lowercase letter")
    print("- Does not contain the phrase “pass” in any format")
    print("- Does not contain the phrase “qwerty” in any format")
    print("- Does not contain the phrase “123”")

    while True:
        password = input("Please Enter the password: ")

        violated_rules = validate_password(password)

        if violated_rules:
            print("This password does not meet the following requirements:")
            for rule in violated_rules:
                print(f"- {rule}")
            print("Please enter a password that conforms to the above restrictions: ")
        else:
            print("Password created Successfully!")
            break

if __name__ == "__main__":
    main()
