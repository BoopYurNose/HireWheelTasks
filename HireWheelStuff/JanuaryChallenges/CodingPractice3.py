'''Count total and unique words in a sentence.

Prompt the user for a sentence.
Normalize to lowercase and strip punctuation.
Split into words and ignore empty tokens.
Output total words and unique word count.'''

# When they say 'Unique word' they mean a word that is different than every other word in the users input

import string

def UniqueWordChecker(SentenceInput):
    FirstWordChar = 0
    TotalWords = 1
    FirstWord = []

    # checks how many words there are overall
    for AllCharacters in SentenceInput:
        if AllCharacters == " ":
            TotalWords += 1


    # I'm gonna take a break from this, make some sorta system where it iterates over each word depending on how many words there are which we checked by checking all the spaces
    # figure out how to all this in a single loop
    for FirstLetters in SentenceInput:
        if FirstLetters.isalnum():
            FirstWord.append(FirstLetters)

        if FirstWord == " " or not FirstLetters.isalnum():
            break

    
    FirstWord = "".join(FirstWord)
    print(FirstWord)



def UserStart():
    print("Welcome to the unique word counter \n")
    UserSentence = input("Type in a sentence: ")

    if not " " in UserSentence:
        print("You need to have more than one word in your sentence Try again: \n")
        UserStart()
        return
    
    if not UserSentence.strip():
        print("You need to have an input Try again: \n")
        UserStart()
        return
    
    for Letters in UserSentence:
        if Letters.isdigit():
            print("You cannot have any numbers in the sentence Try again: \n")
            UserStart()
            return


    UniqueWordChecker(UserSentence.lower())
    


UserStart()