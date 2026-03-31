'''Count total and unique words in a sentence.

Prompt the user for a sentence.
Normalize to lowercase and strip punctuation.
Split into words and ignore empty tokens.
Output total words and unique word count.'''

# When they say 'Unique word' they mean a word that is different than every other word in the users input

import string

def UniqueWordChecker(SentenceInput):
    TotalWords = 1 #initually 1 word because it increments this based on spaces so the first word in the sentence
    # isn't counted because there isn't a space before it, so this defaults at 1 word, if there are no spaces (no other words)
    #in the sentence it'll just stay at 1 word

    for Characters in SentenceInput:
        if Characters == " ":
            TotalWords += 1
    
    print(f"There are {TotalWords} in this sentence")


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
        
    # Figure out how to remove punctation from the sentence
    print(UserSentence)

    UniqueWordChecker(UserSentence)
    


UserStart()