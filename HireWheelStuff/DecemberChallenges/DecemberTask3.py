import math #I'm really confused on this. I'll come back to this later. It somewhat works but not the way I want it to.

#12/21/25 Ive worked on this for like 3 hours trying to understand how it works and how to fix it
# I found the solution online and everything and sure i could just copy and paste the solution here
# and act like I made it but that would do nothing for me, i actually want to uneerstand how eqch part
#of it works without just fucking copying and pasting i actually want to comprehend and understand all of it
# i will work on this more

def NumberChecker(Num):
    if Num < 2:
        print("Sorry You have to choose a number that is above 2 or is 2 itself")
        return
    

    for Num in range(Num, 1, -1):
        Prime = True
        
        for i in range(2, int(math.sqrt(Num)) + 1):
            if Num % i == 0:
                Prime = False
                break
            
            if Prime:
                print(f"{Num} this is a prime number")
            else:
                print(f"{Num} This is not a prime number")
        

        


UserNumber = input("Type in a number to check if it's a prime number or not: ")

if UserNumber.isdigit():
    UserNumber = int(UserNumber)
    NumberChecker(UserNumber)
else:
    print("This is not a number. You need to input only number values")