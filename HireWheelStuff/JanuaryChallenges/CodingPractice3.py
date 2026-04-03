'''Count total and unique words in a sentence.

Prompt the user for a sentence.
Normalize to lowercase and strip punctuation.
Split into words and ignore empty tokens.
Output total words and unique word count.'''

# When they say 'Unique word' they mean a word that is different than every other word in the users input

import string

def UniqueWordChecker(SentenceInput):
    #print(SentenceInput)

    TotalWords = len(SentenceInput.split())
    print(f"You have: {TotalWords} words in your sentence")

    for p in string.punctuation:
        SetenceInput = SentenceInput.replace(p, "")

    Words = (SentenceInput.split())
    print(f"You have 2 unique words in your sentence {len(set(Words))}")

    return

    '''Words = [] Turns out I completely overcomplicated making this, I could've just used basic python string methods the entire time, but I did not know of their existence
    #print(TotalWords)


    # I'm gonna take a break from this, make some sorta system where it iterates over each word depending on how many words there are which we checked by checking all the spaces
    # figure out how to all this in a single loop
    for i in range(0, TotalWords):
        Words.append({i: ""}) # Creating a new table element of every different word in the sentence passed
        print(Words)
        i += 1
        

    Iterator = 0
    for Letters in SentenceInput:
        if Letters == " ":
            print(f"FULL WORD HERE: {Words[Iterator]}")
            Iterator += 1
            print(" ")
        elif Letters.isalnum():
            #print(f"Display this one here {Letters}")
            Words[Iterator] += Letters
            print(f"Adding this to the dictionary {Iterator}: {Words[Iterator]}")

    #print(Words[0])
    

    
    #Words = "".join(Words)
    print(Words)'''



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