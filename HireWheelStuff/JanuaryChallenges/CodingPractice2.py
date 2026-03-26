'''Compute a tip and split the total among a group.

Prompt for bill total, tip percentage, and number of people.
Validate numeric inputs and ensure the group size is at least 1.
Calculate tip amount, total amount, and per-person total (round to 2 decimals).
Print a clear summary with all three values.'''

def Calculator(PartySize, BillTotal, TipPercentage):
    TipPercentage = TipPercentage / 100
    TipPercentage = BillTotal * TipPercentage

    BillTotal = BillTotal + TipPercentage
    
    BillPerPerson = BillTotal / PartySize

    print(f"Your total bill overall is: {round(BillTotal, 2)}")
    print(f"Your bill for {PartySize} people split up is: {round(BillPerPerson, 2)}")
    print(f"And your Tip amount is {round(TipPercentage, 2)}")

def NumberValidator(NumberCheck, FloatsValid):
    if FloatsValid:
        
        try:
            NumberCheck = float(NumberCheck)
            pass
        except:
            return False
        
        if NumberCheck >= 1:
            return True, NumberCheck
        else:
            return False
        
    else:
        
        try:
            NumberCheck = int(NumberCheck)
            pass
        except:
            return False
        
        if NumberCheck >= 1:
            return True, NumberCheck
        else:
            return False
    
    


def UserValueInput():
    print("Welcome to the tip splitter program! \n")
    
    PartySize = input("How many people do you plan on splitting the bill with?: ")
    
    
    if NumberValidator(PartySize, False):
        PartySize = NumberValidator(PartySize, False)[1]
        #print(PartySize)
    else:
        print("Sorry you need to type a number bigger than 1, or type a valid number, or type a int value, not a float number. (float meaning no decimal number Try again: \n")
        UserValueInput()
        return
    
    
    BillTotal = input("Great! what is your total bill?: ")
    
    
    if NumberValidator(BillTotal, True):
        BillTotal = NumberValidator(BillTotal, True)[1]
        #print(BillTotal)
    else:
        print("Sorry you need to type a number bigger than 1, or type a valid number, or type a int value, not a float number. (float meaning no decimal number Try again: \n")
        UserValueInput()
        return
    
    TipPercentage = input("What percentage of the bill are you tipping: ")
    
    if NumberValidator(TipPercentage, True):
        TipPercentage = NumberValidator(TipPercentage, True)[1]
        #print(TipPercentage)
    else:
        print("Sorry you need to type a number bigger than 1, or type a valid number, or type a int value, not a float number. (float meaning no decimal number Try again: \n")
        UserValueInput()
        return
    
    
    Calculator(PartySize, BillTotal, TipPercentage)
    return
    
UserValueInput()
