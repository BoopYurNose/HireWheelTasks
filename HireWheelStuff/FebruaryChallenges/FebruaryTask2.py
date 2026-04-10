#Generate and display the Fibonacci sequence up to N terms.

'''What they mean by N terms is that they are reffering to the user input
if N (userinput) is 5 the program will display the Fibonacci sequence up to 
the number 5
'''

def FibonacciSequence(Amount):
    #print(Amount)

    
    return

def Main():
    print("Welcome to the fibonacci sequence counter \n")

    UserAmount = input("Please input the number value of fibonacci sequence you want the program to output to: ")

    if UserAmount.isdigit():
        pass
    else:
        print("Sorry try again you need to type in a valid whole number for this: \n")
        Main()
        return


    FibonacciSequence(UserAmount)

Main()