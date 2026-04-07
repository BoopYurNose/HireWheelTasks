# Create a password generator that generates a password based on user parameters
# Generate a random password with user-specified length and character types.

# Following inputs
# amount of characters
# allow uppercase?
# allow Numbers characters
import string
import random

def PasswordBuilder(CharacterAmount, Capitalize, AllowNumbers):
    print(CharacterAmount, Capitalize, AllowNumbers)
    
    PresetSettings = [] #Settings value for the for loop make this later

    OnlyCharactersLower = string.ascii_lowercase
    OnlyCharactersLowerNumbers = string.ascii_lowercase + string.digits

    OnlyCharactersAllowsUpper = string.ascii_letters
    AllowAllCharacters = string.ascii_letters + string.digits

    
    for i in range(1, CharacterAmount):
        if Capitalize == True:
            if AllowNumbers == True:
                print("".join(random.choices(AllowAllCharacters, k = 1)))
            else:
                print("".join(random.choices(OnlyCharactersAllowsUpper, k = 1)))
        else:
            if AllowNumbers == True:
                print("".join(random.choices(OnlyCharactersLowerNumbers, k = 1)))
            else:
                print("".join(random.choices(OnlyCharactersLower, k = 1)))
        #print("".join(random.choices(Characters, k = 1)))

        

def Main():
    print("Welcome to the password generator\n")
    PasswordLength = input("How many characters would you want in your password: ")
    
    if PasswordLength.isalnum() and PasswordLength.isnumeric():
        PasswordLength = int(PasswordLength)
        #print("Valid")
    else:
        print("you need to type a valid number Try again \n")
        Main()
        return
    
    Capitalization = False
    AllowUpperCase = input("Would you like uppercase? (y/n): ")
    
    if AllowUpperCase == "y" or AllowUpperCase == "n":
        if AllowUpperCase == "y":
            Capitalization = True
        else:
            pass #Doesn't change boolean value because it's already 
        #pre-set to False so just keeps it the same if user chooses
        # no to capitalization
    else:
        print("only input y for yes or n for no, try again \n")
        Main()
        return
    
    NumbersPermitted = False
    AllowNumbers = input("Would you like to allow special characters? (y/n): ")
    
    if AllowNumbers == "y" or AllowNumbers == "n":
        if AllowNumbers == "y":
            NumbersPermitted = True
        else:
            pass #Doesn't change boolean value because it's already 
        #pre-set to False so just keeps it the same if user chooses
        # no to NumbersPermitted
    else:
        print("only input y for yes or n for no, try again \n")
        Main()
        return
    
    PasswordBuilder(PasswordLength, Capitalization, NumbersPermitted)
            
    
    
Main()
