import random

def GameRetry(CodeList):
    UserListIndex = []
    

    print("\nType in a 4 digits to guess the secretCode\n")
    #print(CodeList)
    
    UserInput = input()
    
    DigitValue = 0
    if not UserInput.isdigit():
        print("Try again you need to type in a digit")
        GameRetry()
        return
    for i in UserInput:
        DigitValue += 1
    if DigitValue != 4:
        print("You need to have a 4 digit guess in your input, please try again")
        GameRetry()
        return

    for UserNum in str(UserInput):
        UserListIndex.append(UserNum)
    # if code gets past here the input is valid


    for i, Num in enumerate(UserListIndex):
        #print(Num)
        if CodeList[i] == Num:
            print("Bull at")
            print(f"Index: {i} Number: {CodeList[i]}")
        elif Num in CodeList: #Doesn't work fix this!!
            print(f"Your cow is numbers {Num}")

    if UserListIndex == CodeList:
        print("Good job you guessed the secret combination!")
        return
    else:
        print("Try again!")
        GameRetry(CodeList)
    

    


def MainGame():
    SecretCodeList = []
    
    
    print("Welcome to the bulls and cows game, you need to guess a random 4 digit code\nfor each digit you get correct you'll get a bulls, but for each digit you get incorrect you'll get a cows")
    
    FirstDigit = random.randint(0, 9)
    SecondDigit = random.randint(0, 9)
    #print(FirstDigit)
    #print(SecondDigit)
    while FirstDigit == SecondDigit:
        #print(f"FirstDigit: {FirstDigit} is the same as SecondDigit: {SecondDigit} Changing that now")
        FirstDigit = random.randint(0, 9)
        #print(FirstDigit)
    ThirdDigit = random.randint(0, 9)
    FourthDigit = random.randint(0, 9)
    while ThirdDigit == FirstDigit or ThirdDigit == SecondDigit or ThirdDigit == FourthDigit:
        ThirdDigit = random.randint(0, 9)
    while FourthDigit == FirstDigit or FourthDigit == SecondDigit or FourthDigit == ThirdDigit:
        FourthDigit = random.randint(0, 9)

    SecretCode = int(str(FirstDigit) + str(SecondDigit) + str(ThirdDigit) + str(FourthDigit))
    
    
    for Numbers in str(SecretCode):
        SecretCodeList.append(Numbers)
        
    
    
    GameRetry(SecretCodeList)
    return
    



MainGame()
