import math #I'm really confused on this. I'll come back to this later. It somewhat works but not the way I want it to.

#12/21/25 Ive worked on this for like 3 hours trying to understand how it works and how to fix it
# I found the solution online and everything and sure i could just copy and paste the solution here
# and act like I made it but that would do nothing for me, i actually want to uneerstand how eqch part
#of it works without just copying and pasting i actually want to comprehend and understand all of it
# i will work on this more

# 3/11/26 UPDATE: I wrote that a long time ago, and as of this date, I came back to this, and solved it easily
# Because I have vastly improved at programming since that previous old date (like 3 months ago)
# I was honestly just over-complicating it, and it was very easy to figure out what I had been doing wrong 

def NumberChecker(Num):
    if Num < 2:
        print("Sorry You have to choose a number that is above 2 or is 2 itself")
        return
    

    for Num in range(2, (Num + 1), 1): # I put Num + 1 so the for loop wouldn't stop at the users original input,
        # Instead it will stop once it outputs the users original value and tells them if it's a prime or not and
        # Once it moves onto the next value (+ 1 after the users input value) the for loop ends there,
        # Maybe this is bad practice, but it does work in my case.
        Prime = True
        if Num % 2 == 0:
            Prime = False

        if Prime or Num == 2:
            print(f"{Num} This is a prime number")
        

        


UserNumber = input("Type in a number to check if it's a prime number or not: ")

if UserNumber.isdigit():
    UserNumber = int(UserNumber)
    NumberChecker(UserNumber)
else:
    print("This is not a number. You need to input only number values")