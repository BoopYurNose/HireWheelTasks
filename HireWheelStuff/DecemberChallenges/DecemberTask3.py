import math #I'm really confused on this. I'll come back to this later. It somewhat works but not the way I want it to.

def NumberChecker(Num):
    if Num >= 2:
        for Num in range(Num, 0, -1):
            for i in range(2, int(math.sqrt(Num)) + 1):
                if Num % i == 0:
                    print(f"sorry {Num} is not a prime number")
                else:
                    print(f"{Num} is a prime number!")
    else:
        print(f"{Num} is not a valid number and it does not have any predecessors of numbers that are prime numbers either")
    

UserNumber = input("Type in a number to check if it's a prime number or not: ")

if UserNumber.isdigit():
    UserNumber = int(UserNumber)
    NumberChecker(UserNumber)
else:
    print("This is not a number. You need to input only number values")