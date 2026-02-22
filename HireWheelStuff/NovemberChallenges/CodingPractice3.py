'''Analyze a sentence and return the first longest word that appears.

Accept a sentence or phrase as input.
Normalize punctuation so words can be compared consistently.
Track the longest word length; if there is a tie, keep the first occurrence.
Return or print the longest word (optionally include its length)'''

WordLengthData = {}

'''for i in range(0, 100):
    print(i)
    WordLengthData[i] = "Test"'''

def WordChecker(Phrase):
    WordCharCount = 0
    WordIndex = 0
    WordEndIndex = 0
    Iterator = 0
    for Character in Phrase:
        if " " in Character:
            print(f"This word is {WordCharCount} Checking next word")
            StartIndex = WordIndex - WordCharCount
            #print(StartIndex)
            #print(WordCharCount)
            WordFound = (Phrase[StartIndex:WordEndIndex])
            print(Iterator)
            WordLengthData[Iterator] = WordFound ,WordCharCount
            WordCharCount = -1
            Iterator += 1
            
        WordCharCount += 1
        WordIndex += 1
        WordEndIndex += 1
        print(f"{WordCharCount} {Character}")
    print(f"The last word is {WordCharCount} characters long")
    StartIndex = WordIndex - WordCharCount
    WordFound = (Phrase[StartIndex:WordEndIndex])
    WordLengthData[Iterator] = WordFound ,WordCharCount

    #Largest = WordLengthData[0]
    Largest = 0

    for Key, Values in WordLengthData.items():
        for Val in Values:
            if isinstance(Val, int): #Getting the number of characters
                #print(Val)
                #Largest = max(Val)
                if int(Val) > Largest:
                    Largest = Val
                    if 
                    
    
    print(Largest)

        

def StartInput():
    print("\nWelcome to the longest word finder \n Type in a phrase")
    
    UserInput = input()
    
    if not UserInput:
        print("\nTry again you need to type in something!")
        #StartInput()
        return
    for Character in UserInput:
        if Character.isnumeric():
            print("\nYou canot have numbers in your input, try again")
            #StartInput()
            return
    WordChecker(UserInput)
# Temporarily hard coded as a variable since the website compiler at school doesn't allow normally this will be a input()

StartInput()
