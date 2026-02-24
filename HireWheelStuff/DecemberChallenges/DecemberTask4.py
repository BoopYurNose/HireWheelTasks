'''Play a number-guessing game where the computer picks a secret 4-digit code with no repeated digits.

Generate a random 4-digit secret code with no repeated digits.
Prompt the user for guesses and validate they are 4 unique digits.
For each guess, calculate Bulls (correct digit in correct position) and Cows (correct digit in wrong position).
Continue until the user guesses correctly or runs out of attempts; display the result.'''
import random

def MainGame():
    print("Welcome to the bulls and cows game, you need to guess a random 4 digit code\nfor each digit you get correct you'll get a bulls, but for each digit you get incorrect you'll get a cows")
    FirstDigit = random.randint(0, 9) #Generate Random Value here
    SecondDigit = random.randint(0, 9)
    #print(FirstDigit)
    #print(SecondDigit)
    while FirstDigit == SecondDigit:
        #print(f"FirstDigit: {FirstDigit} is the same as SecondDigit: {SecondDigit} Changing that now")
        FirstDigit = random.randint(0, 9)
        #print(FirstDigit)
    ThirdDigit = random.randint(0, 9) #Generate Random Value here
    FourthDigit = random.randint(0, 9)
    while ThirdDigit == FirstDigit or ThirdDigit == SecondDigit or ThirdDigit == FourthDigit:
        ThirdDigit = random.randint(0, 9)
    while FourthDigit == FirstDigit or FourthDigit == SecondDigit or FourthDigit == ThirdDigit:
        FourthDigit = random.randint(0, 9)

    SecretCode = int(str(FirstDigit) + str(SecondDigit) + str(ThirdDigit) + str(FourthDigit))
    print("Type in a 4 digit guess to the secretCode")
    UserInput = input()

    if not UserInput.isdigit():
        print("Try again you need to type in a digit")
        MainGame()
        return
    
MainGame()