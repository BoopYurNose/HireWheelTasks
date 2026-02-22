WordLengthData = {}



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
            print(f"Iteration: {Iterator}")
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
        #print(Key, Values)
        for Val in Values:
            if isinstance(Val, int): #Getting the number of characters
                #print(Val)
                #Largest = max(Val)
                if int(Val) > Largest:
                    Largest = Val
                    


    
                    
    
    print(Largest)
    def FindKey(Dictionary, TargetInt):
        if not isinstance(TargetInt, int):
            return
        
        MatchingKeys = [
            key for key, value in Dictionary.items()
            if isinstance(value, (list, tuple)) and len(value) >= 2 and isinstance(value[1], int) and value[1] == TargetInt
        ]

        return MatchingKeys
    

    result = FindKey(WordLengthData, Largest)
    if result:
        IntIndex = result[0]
        print(f"The longest word is {WordLengthData[IntIndex]} characters long")
        return
        



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
