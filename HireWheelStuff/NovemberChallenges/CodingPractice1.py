'''Challenge Overview
Generate an acronym by taking the first letter of each word in a phrase and returning the uppercase result.

Prompt the user for a phrase or sentence.
Split the phrase into words (ignore blank segments or punctuation).
Collect the first letter of each word, uppercase it, and join into the final acronym.
Handle edge cases such as empty input or single-word phrases gracefully.'''

def CreateAcronym(UserPhrase):
    Acronym = (UserPhrase[0:1]) # first letter in the users phrase input
    print(Acronym) #Testing to see if the string sliced the first character in the users input
    IndexValue = 0
    for Letters in UserPhrase:
        IndexValue = IndexValue + 1
        
        #print(IndexValue)
        if " " in Letters:
            NextLetter = (UserPhrase[0:IndexValue+1])
            print(NextLetter)


def UserStart():
    print("welcome to the Acronym creator, Please type in a phrase or sentence")
    UserInput = input()
    if not UserInput:
        print("\nYou need to type in something please try again")
        UserStart()
        return
    elif not (UserInput.isalpha()):
        
        for Character in UserInput:
            if (Character.isdigit()):
                print("\nThis has numbers in it, only type in characters, try again")
                UserStart()
                return
    else:
        print("\nYou need spaces in your phrase try again")
        UserStart()
        return
    
    
    CreateAcronym(UserInput)
    return


UserStart()