def AreaCalculator(Shape):
    if Shape == "sqaure":
        print(f"You have picked {Shape} as your shape")
        UserBase = input("What is your base: ")
        UserHeight = input("What is your height: ")
        if UserBase.isdigit() and UserHeight.isdigit():
            print("this works both are digits")
            UserBase = int(UserBase)
            UserHeight = int(UserHeight)

        SquareArea = UserBase * UserHeight / 2
        print(f"Your area of your {Shape} is {SquareArea}")

AvailableShapes = {
    "Sqaure",
    "Circle",
    "Rectangle",
    "Triangle",
}
def MainMenu():
    print("I can calculate the area of a shape for you. Which shape would you like me to calculate the area of? Here are your options below \n")

    for Shape in AvailableShapes:
        print(Shape)

    UserInput = input("Type in one of the options above!:")

    for Shapes in AvailableShapes:
        if UserInput.lower() in Shapes.lower():
            AreaCalculator(UserInput.lower())

MainMenu()