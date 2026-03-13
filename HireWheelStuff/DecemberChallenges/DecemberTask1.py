'''Challenge Overview
Determine whether two strings are anagrams of each other, ignoring spaces, punctuation, and capitalization.

Prompt the user for two strings to compare.
Normalize both strings by removing spaces, punctuation, and converting to lowercase.
Compare the sorted characters of each string to determine if they are anagrams.
Print a clear message indicating whether the strings are anagrams.'''

'''Initially I knew how to create this, I would just create a list that had every single letter in the alphabet,
then I would iterate both word inputs through this for loop that would check for the same characters, but this is
honestly fucking stupid, not only is it likely to not work, for various reasons, but additionally, it's overcomplicating it
A significantly better way to do this, is append both word inputs into list values, and have for loops that will iterate through
the first letter index, and check if the other word has the first letter index in it aswell (I may not even have to create 2 seperate
lists for this)

I don't even have to create 2 seperate lists, I can just iterate through each letter in the first word input and compare each 
individual letter in the FirstWordInput to the first letter in the 2nd word, I can reference the first letter in the 2nd word
by converting each letter in the SecondWord into a list, and each time a match is found the i variable (which stand for iterator)
is increased by + 1 it'll move onto the next index inside the list'''

''' if you were to create an emptyy list like this
IndividualLetters = []

then add elements to it
    for Letters in SecondWord:
        IndividualLetters.append(Letters)

Question to ask later: In python Will the initial definition of the empty list make index 0 (the first index) of the list equal to []
 how come it's not equal to the first element added to the list

 because when I try to print 
 print(IndividualLetters[0:0])

 shouldn't it just print the first element added to the list?
 and not [], why does that happen?

I realized even my "less overcomplicated way" of doing it, will not work, I could technically get it to work, but I realized there's a much
simplier solution, I don't even need to iterate through the list index for the second word, I simply just need to do a if FirstWordLetters in SecondWordLetters:
simply an "if in" statement, I don't know why I didn't think about this earlier, but it works now,
'''

import string

def CheckAnagram(FirstWord, SecondWord):
    FirstWordLetterAmount = len(FirstWord)
    #print(FirstWordLetterAmount)
    IndividualLetters = []
    for Letters in SecondWord:
        IndividualLetters.append(Letters)

    #print(IndividualLetters)

    IntCharacterValue = (len(IndividualLetters))
    i = 1
    #print(IndividualLetters[0:1])

    if FirstWordLetterAmount == IntCharacterValue:
        print("both have same length of characters")
        for CharacterLetters in FirstWord:
            print(CharacterLetters)
            if CharacterLetters in (IndividualLetters):
                print(f"Word {CharacterLetters} match")
                i += 1

            if i == (FirstWordLetterAmount + 1):
                print("The strings are anagrams")
                return
    print("The strings are not anagrams")
    return
    





def StartGame():
    print("Welcome to the anagram checker! \n")
    FirstWord = input("\n Please input your first word: ")

    for Letters in FirstWord:
        if Letters.isdigit():
            print("\n Try again you need to type in an actual word, with characters in it, no numbers")
            StartGame()
            return
        elif Letters in string.punctuation:
            print("\n Try again you need to have a word without any punctuation")
            StartGame()
            return
        
    SecondWord = input("\n Please input your second word: ")

    for Letters in SecondWord:
        if Letters.isdigit():
            print("\n Try again you need to type in an actual word, with characters in it, no numbers")
            StartGame()
            return
        elif Letters in string.punctuation:
            print("\n Try again you need to have a word without any punctuation")
            StartGame()
            return

        
    # NOTE: make it remove spaces, punctiation, etc before passing it as a function arguement
    # do this later, for now, just manually not input any of those listed

    CheckAnagram(FirstWord.lower(), SecondWord.lower())
        
    
    
    
StartGame()