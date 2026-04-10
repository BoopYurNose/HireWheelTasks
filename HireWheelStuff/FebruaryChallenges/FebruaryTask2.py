#Generate and display the Fibonacci sequence up to N terms.
# This was a lot easier than I thought it would be :3

'''What they mean by N terms is that they are reffering to the user input
if N (userinput) is 5 the program will display the Fibonacci sequence up to 
the number 5
'''

def FibonacciSequence(Amount):
    StartingSequence = [0, 1]
    while len(StartingSequence) < Amount:
        StartingSequence.append(StartingSequence[-1] + StartingSequence[-2])
    
    return StartingSequence

def Main():
    print("Welcome to the fibonacci sequence counter \n")

    UserAmount = input("Please input the number value of fibonacci sequence you want the program to output to (type a number bigger than 1 please): ")

    if UserAmount.isdigit():
        pass
        UserAmount = int(UserAmount)
        if UserAmount <= 1:
            print("Please type a number bigger than 1 try again: \n")
            Main()
            return
    else:
        print("Sorry try again you need to type in a valid whole number for this: \n")
        Main()
        return


    print(FibonacciSequence(UserAmount))

Main()