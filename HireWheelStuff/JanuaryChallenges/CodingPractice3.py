'''Count total and unique words in a sentence.

Prompt the user for a sentence.
Normalize to lowercase and strip punctuation.
Split into words and ignore empty tokens.
Output total words and unique word count.'''

# When they say 'Unique word' they mean a word that is different than every other word in the users input

import string

def UniqueWordChecker(SentenceInput):

    TotalWords = len(SentenceInput.split())
    Words = []
    print(TotalWords)


    # I'm gonna take a break from this, make some sorta system where it iterates over each word depending on how many words there are which we checked by checking all the spaces
    # figure out how to all this in a single loop
    for i in range(0, TotalWords):
        for FirstLetters in SentenceInput:
            if FirstLetters.isalnum():
                Words.append(FirstLetters)

            if Words == " " or not FirstLetters.isalnum():
                Words.append(", ")
                break
    

    
    Words = "".join(Words)
    print(Words)



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