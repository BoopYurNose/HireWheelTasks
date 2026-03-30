'''Challenge Overview
Score a multiple-choice quiz from an answer key and user answers.

Prompt for the answer key as a comma-separated list (A/B/C/D).
Prompt for the user's answers in the same format.
Compare answers position-by-position and count correct responses.
Output the score as a count and percent; handle mismatched lengths gracefully.'''

def ScoreOutput(AnswerKey, AnswerInputs):
    Score = 0
    TotalQuestions = len(AnswerKey)
    #print(TotalQuestions)
    for i in range(0, TotalQuestions):
        try:
            AnswerKey[i]
            AnswerInputs[i]
        except:
            return (f"You got {Score}/{TotalQuestions} Correct! Also keep in mind you only answered {len(AnswerInputs)} questions, out of the {TotalQuestions} provided, \n the ones you didn't answer at all were counted incorrect \n next time make sure to answer all questions")
        if AnswerKey[i] == AnswerInputs[i]:
            print(AnswerKey[i], AnswerInputs[i])
            print("This is correct! \n")
            Score += 1
        else:
            print(AnswerKey[i], AnswerInputs[i])
            print("This is not correct \n")

    return (f"You got {Score}/{TotalQuestions} correct!")
        

def Validator(KeysPassed): #This will get the first letter of each character after a comma for the user input, so even if they mistakenly type like A, BC, C it'll still only count the first character after a comma
    KeysList = []
    AddCharacter = False
    for Char in KeysPassed:
        if Char.isnumeric():
            return False

        if AddCharacter == False:
            if not Char == " ":
                KeysList.append(Char)
                AddCharacter = True
            
        
        if Char == ",":
            AddCharacter = False
        #print(KeysList)

    return True, KeysList

def PromptUser():
    print("Welcome to the Quiz Scorekeeper, please input the following:")

    UserAnswerKey = input("Please input your answer key as a comma seperated list: ")

    if Validator(UserAnswerKey):
        UserAnswerKey = Validator(UserAnswerKey)[1]
        #print(UserAnswerKey)
    else:
        print("Try again every letter needs to be a character")
        PromptUser()
        return

    UserAnswer = input("Now type in your answers for the Quiz!: ")

    if Validator(UserAnswer):
        UserAnswer = Validator(UserAnswer)[1]
        #print(UserAnswer)
    else:
        print("Try again every letter needs to be a character")
        PromptUser()
        return

    print(ScoreOutput(UserAnswerKey, UserAnswer))




PromptUser()