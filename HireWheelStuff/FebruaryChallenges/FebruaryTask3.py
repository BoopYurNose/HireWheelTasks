'''Caesar Cipher
Encrypt or decrypt a message by shifting each letter by a fixed number of positions in the alphabet.'''

'''How the Ceasar Cipher works
The Ceaser Cipher works by taking the position of a character in the alphabet for example
A --> D
shifting it 3 positions to the left to encrypt the message
Another example is 
ABC --> DEF'''




def InputValidator(Input):
    if not Input.strip():
        print("Try again you need to type in some word or some character: \n")
        Main()
        return False
    for Characters in Input:
        if Characters.isdigit():
            print("Try again you cannot have any numbers in your input: \n")
            return False
    
    #if users input is validated




def Main():
    print("Welcome to the Ceasar Cipher Encryptor program \n would you like to either Encrypt a message, or Decrypt a message")

    UserChoice = input("Type: Encrypt or Decrypt: ")
    #print(type(UserChoice))

    if UserChoice.lower() != "encrypt" and UserChoice.lower() != "decrypt":
        print("Try again, you need to type in a a valid input of only Encrypt or Decrypt \n")
        Main()
        return
        
    if UserChoice.lower() == "encrypt":
        UserInput = input("Type in the message you would like to encrypt: ")
        if not InputValidator(UserInput):
            Main()
            return
    elif UserChoice.lower() == "decrypt":
        UserInput = input("Type in the message you would like to decrypt: ")
        if not InputValidator(UserInput):
            Main()
            return


Main()