'''Create a program that first asks the user which temperature scale they would like to convert from
(e.g., Celsius, Fahrenheit, Kelvin).
Then, ask which temperature scale they would like to convert to.
Afterward, prompt the user for the temperature value and perform the conversion.'''

Options = [
    "celsius",
    "fahrenheit",
    "kelvin",
]

def Calculations(ConvertFrom, Value, ConvertTo):
    if ConvertFrom == ConvertTo:
        print(f"You tried to convert the same temperature value to eachother. They'll just be the same value regardless. Anyways the value is {Value}")
        return
    
    #User converting celsius to another temp value

    if ConvertFrom.lower() == "celsius" and ConvertTo.lower() == "fahrenheit":
        ConvertValue = Value * 1.8 + 32
        print(f"Your {ConvertFrom} value of {Value} converted to {ConvertTo} is {ConvertValue}")
        return
    elif ConvertFrom.lower() == "celsius" and ConvertTo.lower() == "kelvin":
        ConvertValue = Value + 273.15
        print(f"Your {ConvertFrom} value of {Value} converted to {ConvertTo} is {ConvertValue}")
        return

    #User converting fahrenheit to another temp value    

    if ConvertFrom.lower() == "fahrenheit" and ConvertTo.lower() == "celsius":
        ConvertValue = Value - 32 * 5 / 9
        print(f"Your {ConvertFrom} value of {Value} converted to {ConvertTo} is {ConvertValue}")
        return
    elif ConvertFrom.lower() == "fahrenheit" and ConvertTo.lower() == "kelvin":
        ConvertValue = Value / 1.8 + 273.15
        print(f"Your {ConvertFrom} value of {Value} converted to {ConvertTo} is {ConvertValue}")
        return

    #User converting kelvin to another temp value    

    if ConvertFrom.lower() == "kelvin" and ConvertTo.lower() == "celsius":
        ConvertValue = Value - 273.15
        print(f"Your {ConvertFrom} value of {Value} converted to {ConvertTo} is {ConvertValue}")
        return
    elif ConvertFrom.lower() == "kelvin" and ConvertTo.lower() == "fahrenheit":
        ConvertValue = Value * 1.8 - 459.67
        print(f"Your {ConvertFrom} value of {Value} converted to {ConvertTo} is {ConvertValue}")
        return






def StartMenu():
    print("Hello welcome to the Temperature scale converter! Here are your options below.")

    for Choice in Options:
        print(Choice)

    UserConvertFrom = input("What would you like to convert from pick one of the options above:")
    UserValue = input("Now please type in a number value of the tempurature you'd like to convert from:")
    UserConvertTo = input("Now type the temperature unit you'd like to convert to:")

    if (UserValue.isdigit()):
        UserValue = int(UserValue)
    else:
        print("Not a valid digit try again")
        return
    
    if UserConvertFrom.lower() in Options:
        print(f"You are converting from {UserConvertFrom}")
    else:
        print("You need to type in a valid temperature unit. Try again")
        return
    
    if UserConvertTo.lower() in Options:
        print(f"to {UserConvertTo}")
    else:
        print("You need to type in a valid temperature unit. Try again")
        return
    
    Calculations(UserConvertFrom, UserValue, UserConvertTo)

        
    



StartMenu()