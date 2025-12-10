UserAttempts = 0
UserLimit = 3

SecretWord = "amelia"

SecretWordReversed = SecretWord[::-1]

print(f"Welcome to the guessing game try to guess this word. Except it is reversed {SecretWordReversed} good luck")

while UserAttempts < UserLimit:
    UserInput = input()
    if UserInput == SecretWord:
        print(f"good job you guessed the secret word it was {SecretWord}")
        break
    elif UserInput != SecretWord:
        UserAttempts += 1
        print(f"Nope try again you have {UserLimit - UserAttempts} tries left")



if UserInput != SecretWord:
    print(f"You have {UserLimit - UserAttempts} left you did not guess the secret word")