def Addition(FirstNumber, SecondNumber):
    print(f"This is your answer for Addition {FirstNumber + SecondNumber}")

def Subtraction(FirstNumber, SecondNumber):
    print(f"This is your answer for Subtraction {FirstNumber - SecondNumber}")

def Division(FirstNumber, SecondNumber):
    print(f"This is your answer for Division {FirstNumber / SecondNumber}")

def Multiplication(FirstNumber, SecondNumber):
    print(f"This is your answer for Multiplication {FirstNumber * SecondNumber}")

AcceptableOperations = [
    "+",
    "-",
    "*",
    "/",
]

FirstUserInput = "Nothing"

while not isinstance(FirstUserInput, (int, float, complex)): # Checks if the FirstUserInput variable is a number value or not while its not a number value it will continue repeating itself until user inputs number value
    print("Type in your first number for the operation")
    FirstUserInput = input()

    if FirstUserInput.isnumeric(): #string based check. Checks if the string contains numbers if it does it converts the string to a number value
        FirstUserInput = int(FirstUserInput)
        print("Good that works!")
    else:
        print("Try again you need a number value")

SecondUserInput = "Nothing"

while not isinstance(SecondUserInput, (int, float, complex)):
    print("Now type in your second number for the operation")
    SecondUserInput = input()
    if SecondUserInput.isnumeric():
        SecondUserInput = int(SecondUserInput)
    else:
        print("Try again you need to type in a number value")

OperationSelection = "Nothing"

while OperationSelection not in AcceptableOperations: # checks if variable OperationSelection has a value equal to string values in AcceptableOperations table loops until OperationSelection has value equal to a string value in the table AcceptableOperation
    print("Now type in your operation type either + - * /")
    OperationSelection = input()
    if OperationSelection == "+":
        Addition(FirstUserInput, SecondUserInput)
    elif OperationSelection == "-":
        Subtraction(FirstUserInput, SecondUserInput)
    elif OperationSelection == "/":
        Division(FirstUserInput, SecondUserInput)
    elif OperationSelection == "*":
        Multiplication(FirstUserInput, SecondUserInput)
    else:
        print("Try again you need to type a single operation exactly how its shown its case sensetive")