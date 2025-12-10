ShoppingList = {
    "Water",
    "Chicken",
    "Rice",
    "Laptop",
    "Gas"
}

ItemToCheck = {
    "Water",
    "Money",
    "Rice",
    "Bottle",
    "Chicken",
    "Gas"
}

for Key, Value in ipairs(ShoppingList) do
    for k, v in ipairs(ItemToCheck) do
        if Value == v then
            print("Your items to check has "..v)
        end
    end
end