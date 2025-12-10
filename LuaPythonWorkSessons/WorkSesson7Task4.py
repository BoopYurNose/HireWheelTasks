ShoppingList = [
    "Bottle",
    "Gas",
    "Chicken",
    "Rice",
    "Meat"
]

ItemList = [
    "HotDog",
    "Water",
    "Gas",
    "Oxygen",
    "Power",
    "Meat"
]

for Item in ShoppingList:
    for List in ItemList:
        if Item == List:
            print(f"You have {List} in your itemlist thats also on the shopping list")