FirstTable = {
    Key1 = "First key Input",
    Key2 = "Another Key Input",
    Key3 = "Third Key thingy",
    Key4 = "A fourth one Key Input",
    Key5 = "A fifth one random thing",
    Key6 = "Another one at last",
    Key7 = "This is just a test",
    Key8 = "I really enjoy programming and this is my last test",
}

PrintingTable = {} -- empty table

for i = 1, 12 do -- a loop that runs 12 times
    local Key = "Key"..i -- Making Key variable equal to Key1, Key2, etc
    local Value = FirstTable[Key] -- Creating Value variable and referencing the FirstTable so we can get our string values
    table.insert(PrintingTable, Value) -- inserting the value variables into a new table and this table can use ipairs since it only takes in the string values
end

for k, v in ipairs(PrintingTable) do -- iterating over all the PrintingTable values
    print("Key"..k,v) -- printing key string then the itarator of the ipairs then the string value
end
