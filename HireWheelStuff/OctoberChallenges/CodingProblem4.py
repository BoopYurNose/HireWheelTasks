import random


def NumberRangeCheck(NumberInput):
    if NumberInput >= 1 and NumberInput <= 100:
        return True
    else:
        return False
    


    
def MainGame(NumberInputMain):
    if (NumberInputMain.isdigit()):
        print("\nGreat this is a number value, good job!")
    else:
        print("Sorry you need to type an actual number value. Try again")
        return
    

    RandomValue = random.randint(1, 100)
    #print(RandomValue)
    UserAttempts = 1 #It equals one because it doesn't count the first one because your first guess isn't inside the function 

    NumberInputMain = int(NumberInputMain)
    if NumberRangeCheck(NumberInputMain):
        print("This number is also in range of 1 - 100! Great!")
        while NumberInputMain != RandomValue:
            UserAttempts = UserAttempts + 1
            if NumberInputMain > RandomValue:
                print("Your guess is higher than the random value, try again")
                NumberInputMain = input("Guess again here: ")
                NumberInputMain = int(NumberInputMain)
            else:
                print("Your guess is lower than the random value, try again")
                NumberInputMain = input("Guess again here: ")
                NumberInputMain = int(NumberInputMain)
        print(f"Amazing job! you guessed the number it was {RandomValue} \n It only took you {UserAttempts} tries to guess the secret number.")
        





    else:
        print("Sorry you need to type a number within the range of 1 - 100. Try again")
    

UserInput = input("Hello, Guess a number from 0 - 100:")
MainGame(UserInput)