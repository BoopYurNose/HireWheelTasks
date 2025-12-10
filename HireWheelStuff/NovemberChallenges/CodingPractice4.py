'''Write a program that lets the user play a single round of Rock, Paper, Scissors against the computer.
 The computer should randomly choose one of the three options, and then the user will be prompted for their choice.
   The program then announces the result (win, lose, or draw).'''

import random

AvailableOptions = [
    "Rock",
    "Paper",
    "Scissors",    
]

def MainGame(UserChoice):
    BotChoice = random.choice(AvailableOptions)
    if UserChoice.lower() == BotChoice:
        print(f"\n You both picked {BotChoice}: Draw")

    elif UserChoice.lower() == "rock" and BotChoice.lower() == "paper":
        print(f"\n You picked {UserChoice} and Bot picked {BotChoice}: You lose")
    elif UserChoice.lower() == "rock" and BotChoice.lower() == "scissors":
        print(f"\n You picked {UserChoice} and Bot picked {BotChoice}: You Win")

    elif UserChoice.lower() == "paper" and BotChoice.lower() == "scissors":
        print(f"\n You picked {UserChoice} and Bot picked {BotChoice}: You lose")
    elif UserChoice.lower() == "paper" and BotChoice.lower() == "rock":
        print(f"\n You picked {UserChoice} and Bot picked {BotChoice}: You Win")

    elif UserChoice.lower() == "scissors" and BotChoice.lower() == "rock":
        print(f"\n You picked {UserChoice} and Bot picked {BotChoice}: You lose")
    elif UserChoice.lower() == "scissors" and BotChoice.lower() == "paper":
        print(f"\n You picked {UserChoice} and Bot picked {BotChoice}: You Win")

    print("Going back to StartMenu")
    StartMenu()



def StartMenu():
    print("Welcome to Rock Paper Scissors. You can pick one of the options below  by typing it in or type Quit to end the program\n")
    for Option in AvailableOptions:
        print(Option)

    UserInput = input("Type in your choice: ")

    for Option in AvailableOptions:
        if UserInput.lower() == Option.lower():
            MainGame(UserInput)
            return
        
    
    if UserInput == "Quit":
        return
    else:
        print("Try again you need to type in one of the options provided on screen")
        StartMenu()

    

    


StartMenu()