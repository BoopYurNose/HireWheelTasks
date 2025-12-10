-- I wanted to remake this becuase I failed to relize how fucking ass the way I coded the other one

NoteStorage = {
    ["Note1"] = "",
    ["Note2"] = "",
    ["Note3"] = "",
    ["Note4"] = "",
    ["Note5"] = "",
    ["Note6"] = "",    
    ["Note7"] = "",
    ["Note8"] = "",
    ["Note9"] = "",
    ["Note10"] = "",
}

UserOptions = {
    "NoteView",
    "NoteDelete",
    "NoteAdd",
}

FunctionAmount = 0

function StartMenu()
    print("Options \n NoteView \n NoteDelete \n NoteAdd")
    UserChoice = io.read()

    OptionCheck(UserOptions, UserChoice)


    if OptionCheck(UserOptions, UserChoice) then
        print("This works") -- pass a function call here depending on what the user choice was
    elseif OptionCheck(UserOptions, UserChoice) == false then
        print("Try again that wasn't right")
        StartMenu()
    end
    
end

function OptionCheck(Table, UserInput)
    FunctionAmount = FunctionAmount + 1
    print("OptionsCheck function called "..FunctionAmount) -- this is simply just to see how many times it fires the function
    for _, Value in pairs(Table) do
        if UserInput == Value then
            return true
        end
    end
    return false
end

StartMenu()