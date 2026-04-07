# Create a password generator that generates a password based on user parameters
# Generate a random password with user-specified length and character types.

# Following inputs
# amount of characters
# allow uppercase?
# allow special characters

def Main():
    print("Welcome to the password generator")
    PasswordLength = input("How many characters would you want in your password: ")
    
    if PasswordLength.isalnum():
        if PasswordLength.isnumeric():
            print("This is valid")
            
    
    
Main()
