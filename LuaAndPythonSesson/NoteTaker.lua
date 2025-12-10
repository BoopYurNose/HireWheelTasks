NoteStorageTable = {
    Note1 = "nil",
    Note2 = "nil",
    Note3 = "nil",
    Note4 = "nil",
    Note5 = "nil",
    Note6 = "nil",
    Note7 = "nil",
    Note8 = "nil",
    Note9 = "nil",
    Note10 = "nil",
    Note11 = "nil",
    Note12 = "nil",
}

NoteIncrement = 0 -- Starting value for how many notes you've created


function StartingMenu()

    ScriptEnded = false
    print("Welcome to the MainMenu of the NoteTaker what would you like to do? \n \n CreateNewNote \n NoteStorage \n NoteDelete \n EndScript")
    
    local UserChoice = io.read()
    if UserChoice == "CreateNewNote" then
        CreateNote()
        elseif UserChoice == "NoteStorage" then
            NoteStorage()
            elseif UserChoice == "NoteDelete" then
                NoteDelete()
                elseif UserChoice == "Endscript" then
                    print("Alright script is ending goodbye!")
                    ScriptEnded = true -- bug here
                    return
                        else
                        print("Try again you need to type it exactly how its printed becuase its case sensitive")
                        StartingMenu()
    end
end

function CreateNote()

    if NoteIncrement <= 0 then
        NoteIncrement = 1
    end

    -- add a feature where you can pick what note number to input and it'll change the note increment based on that so you can pick to make a note in note1 or note2

    print("Welcome to the CreateNote menu pick a NoteIncrement to write your note on here are the choices")

    -- print the notes
    local PrintingTable = {}

    for i = 1, 12 do
        local KeyValue = "Note"..i
        local Value = NoteStorageTable[KeyValue]
        table.insert(PrintingTable, Value)
    end

    for k, v in ipairs(PrintingTable) do
        print("Note"..k, v)
    end

    print("type a number from 1 - 12 to pick a note slot to input a note in")

    UserIncrementInput = io.read()
    UserIncrementInput = tonumber(UserIncrementInput)
    if UserIncrementInput < 1 or UserIncrementInput > 12 then
        print("You have to type a number between 1 and 12 returning to starting menu.. try again")
        StartingMenu()
        return
    else
        NoteIncrement = UserIncrementInput
    end


    print("Welcome to the CreateNote menu you are currently on your note"..NoteIncrement.." type anything for this note")
    NoteInput = io.read()
    if NoteIncrement == 1 then
        NoteStorageTable["Note1"] = NoteInput
    elseif NoteIncrement == 2 then
        NoteStorageTable["Note2"] = NoteInput
    elseif NoteIncrement == 3 then
        NoteStorageTable["Note3"] = NoteInput
    elseif NoteIncrement == 4 then
        NoteStorageTable["Note4"] = NoteInput
    elseif NoteIncrement == 5 then
        NoteStorageTable["Note5"] = NoteInput 
    elseif NoteIncrement == 6 then
        NoteStorageTable["Note6"] = NoteInput
    elseif NoteIncrement == 7 then
        NoteStorageTable["Note7"] = NoteInput
    elseif NoteIncrement == 8 then
        NoteStorageTable["Note8"] = NoteInput
    elseif NoteIncrement == 9 then
        NoteStorageTable["Note9"] = NoteInput
    elseif NoteIncrement == 10 then
        NoteStorageTable["Note10"] = NoteInput
    elseif NoteIncrement == 11 then
        NoteStorageTable["Note11"] = NoteInput
    elseif NoteIncrement == 12 then
        NoteStorageTable["Note12"] = NoteInput
    end

    print("Your note"..NoteIncrement.." has been saved as: "..NoteInput.." :returning to StartingMenu")
    StartingMenu()
end



function NoteStorage()

    local NewTable = {}

   print("Welcome to the note storage here are your saved notes \n")
   for i = 1, 12 do -- iterating 12 times (looping 12 times)
    local NumberKeyValue = "Note"..i -- Subbing in the i = (1-12) at the end of each "Note" string so creating "Note1", "Note2", etc
    local Values = NoteStorageTable[NumberKeyValue] --[[Creating a new variable called Values which references the NoteStorageTable
    (how we get the string values of NoteStorageTable when calling NewTable) and making Values variable equal to NoteStorageTable["Note1"], NoteStorageTable["Note2"], etc ]]
    table.insert(NewTable, Values) -- creates a new table called NewTable and inserts the Values Variable into it calling the string values from NoteStorageTable
   end

    for k, v in ipairs(NewTable) do -- Calling the key and value and iterating over each key and value
    
        if v ~= "nil" then
            print("Note"..k, v) -- printing "Note" with corrisponding ipairs iteration after it so it looks like Note1, Note2, etc and printing the string values from NoteStorageTable
            
        elseif v == "nil" then
            print("Note"..k.." This note slot is empty") -- for every note that isn't inputted yet its tells user that it is empty
        end
    end

    print("\n Returning to Starting Menu")

    StartingMenu()

end

function NoteDelete()
    print("Welcome to the Note Delete menu here are your current notes")

    local PrintTable = {}

    for i = 1, 12 do -- loops 12 times
        local Keys = "Note"..i -- Creates 12 different "Note" strings with adding the number everytime incrementing up to 12 like Keys = "Note1", "Note2", etc
        local Values = NoteStorageTable[Keys] -- Values variable and referencing the original NoteStorageTable and subbing in the keys to get the string values
        table.insert(PrintTable, Values) -- Inserting the string values into the new key with only one string value in each different table input allowing us to use ipairs on this table
    end

    for k,v in ipairs(PrintTable) do -- iterating over all string values stored in here
        if v ~= "nil" then -- printing Note then ipairs increment value then the string value
        print("Note"..k,v)
        end
    end

    print("Which note would you like to delete type in a number from 1-12 and it will be deleted otherwise if you'd like to go back to startmenu type NoDelete")

    local UserInput = io.read()
    
    if UserInput == "NoDelete" then
        print("User decided to not delete a note returning to StartingMenu")
        StartingMenu()
    else
        UserInput = tonumber(UserInput)
        if UserInput > NoteIncrement then
            print("You don't have a note slot there going back to StartingMenu")
            StartingMenu()
        elseif UserInput <= NoteIncrement then
            NoteStorageTable["Note"..UserInput] = "nil"
            print("Note"..UserInput.." has been deleted it now equals "..NoteStorageTable["Note"..UserInput])
            NoteIncrement = NoteIncrement - 1
            StartingMenu()
        end
    end


end


if ScriptEnded == false then
    StartingMenu()
elseif ScriptEnded == true then
    print("cyaaaa!!!")
end
