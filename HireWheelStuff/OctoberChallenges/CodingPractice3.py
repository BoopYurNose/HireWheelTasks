def UniqueWordChecker(WordText):
    if len(WordText) == len(set(WordText)):
        print(f"Every character in this word {WordText} is a unique character")
    else:
        print(f"Every character in this word {WordText} is not a unique character")
    
print("Hello, welcome to the Unique Characters checker, \n This will check if all of your characters in the string that you input are all unique from eachother ")

UserInput = input("Type in your characters:")


UniqueWordChecker(UserInput)