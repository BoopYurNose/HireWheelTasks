import math #I'm really confused on this. I'll come back to this later. It somewhat works but not the way I want it to.

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