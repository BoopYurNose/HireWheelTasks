'''Count total and unique words in a sentence.

Prompt the user for a sentence.
Normalize to lowercase and strip punctuation.
Split into words and ignore empty tokens.
Output total words and unique word count.'''

# When they say 'Unique word' they mean a word that is different than every other word in the users input

import string

def UniqueWordChecker(SentenceInput):
    FirstWordChar = 0
    FirstWord = []

    for LettersFirst in SentenceInput:
        FirstWordChar += 1
        FirstWord.append(LettersFirst)
        if LettersFirst == " ":

            break

        FirstWord = "".join(FirstWord)

    print(f"First word has {FirstWordChar} characters")
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
        
    # Figure out how to remove punctation from the sentence
    print(UserSentence.split())

    UniqueWordChecker(UserSentence)
    


UserStart()