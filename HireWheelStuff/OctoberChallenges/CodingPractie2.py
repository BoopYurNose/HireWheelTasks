def AreaCalculator(Shape):
    pass

AvailableShapes = {
    "Sqaure",
    "Circle",
    "Rectangle",
    "Triangle",
}

print("I can calculate the area of a shape for you. Which shape would you like me to calculate the area of? Here are your options below \n")

for Shape in AvailableShapes:
    print(Shape)

UserInput = input("Type in one of the options above!:")

for Shapes in AvailableShapes:
    if UserInput.lower() != Shapes.lower():
        print("Sorry, this is not an option on the available shapes")
        break
    else:
        print("This works great!")
        break