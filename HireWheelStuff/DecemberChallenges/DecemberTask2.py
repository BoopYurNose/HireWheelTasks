BMIIndex = {
    "UnderWeight": 18.5, #Below this is UnderWeight
    "Normal": 24.9, #Below this but above 18.5 is Normal
    "OverWeight": 29.9, #Below this but above 24.9 is OverWeight
    "Obese": 34.9, #Below this but above 29.9 is Obese
    "Extremely_Obese": 35 #Above this is Extremely Obese
}

def BMICheck(Height, Weight):
    Height = float(Height)
    Weight = float(Weight)
    
    BMI = Weight / (Height ** 2)
    BMI = (round(BMI, 2))
    print(f"Your BMI is: {BMI}")
    for Classification in BMIIndex:
        if BMI < BMIIndex["UnderWeight"]:
            print("You are UnderWeight")
            break
        elif BMI < BMIIndex["Normal"]:
            print("You are Normal")
            break
        elif BMI < BMIIndex["OverWeight"]:
            print("You are OverWeight")
            break
        elif BMI < BMIIndex["Obese"]:
            print("You are Obese")
            break
        elif BMI >= BMIIndex["Extremely_Obese"]:
            print("You are Extremely_Obese")
            break



def StartMenu():
    print("Welcome to the BMI calculator. \n Please input your height in meters")
    UserHeight = input()
    
    try:
        float(UserHeight)
        if float(UserHeight) <= 0:
            print("Sorry not a valid number range, try again")
            StartMenu()
            return
    except ValueError:
        print("Sorry this is not a valid value, try again")
        StartMenu()
        return

    print("Great job! Now input your weight in kilograms")
    UserWeight = input()

    try:
        float(UserWeight)
        if float(UserWeight) <= 0:
            print("Sorry not a valid number range, try again")
            StartMenu()
            return
    except ValueError:
        print("Sorry this is not a valid value, try again")
        StartMenu()
        return

    print("Great all checks out!")
    BMICheck(UserHeight, UserWeight)
    


StartMenu()