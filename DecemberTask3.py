def NumberChecker(Num):
    if Num >= 2:
        pass # math stuff here
    else:
        print(f"{Num} is not a valid number and it does not have any predecessors of numbers that are prime numbers either")
    

UserNumber = input("Type in a number to check if it's a prime number or not: ")

if UserNumber.isdigit():
    UserNumber = int(UserNumber)
    NumberChecker(UserNumber)
else:
    print("This is not a number. You need to input only number values")