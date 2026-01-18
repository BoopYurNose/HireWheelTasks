def AreaCalculator(Shape):
    print(f"You have picked {Shape} as your shape")
    if Shape == "rectangle":
        UserBase = input("What is your base: ")
        UserHeight = input("What is your height: ")
        if UserBase.isdigit() and UserHeight.isdigit():
            UserBase = int(UserBase)
            UserHeight = int(UserHeight)
            RectangleArea = UserBase * UserHeight
            print(f"Your area of your {Shape} is {RectangleArea}")
            return
        

    elif Shape == "square":
        UserLength = input("What is your Length: ")
        if UserLength.isdigit():
            UserLength = int(UserLength)
            SquareArea = UserLength * UserLength
            print(f"Your area of your {Shape} is {SquareArea}")
            return
        
    elif Shape == "triangle":
        UserBase = input("What is your base: ")
        UserHeight = input("What is your height: ")
        if UserBase.isdigit() and UserHeight.isdigit():
            UserBase = int(UserBase)
            UserHeight = int(UserHeight)
            TriangleArea = UserBase * UserHeight / 2
            print(f"Your area of your {Shape} is {TriangleArea}")
            return
        
    elif Shape == "circle":
        UserRadius = input("What is your radius: ")
        if UserRadius.isdigit():
            UserRadius = int(UserRadius)
            UserRadius = UserRadius * UserRadius
            CircleArea = UserRadius * 3.14
            print(f"Your area of your {Shape} is {CircleArea}")
            return



AvailableShapes = {
    "Square",
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