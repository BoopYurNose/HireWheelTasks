UserMoney = 100

UserOptions = {
    "CheckBalance",
    "Deposite",
    "Withdraw",
    "Quit",
}



function StartMenu()
    print("Welcome to the banking start menu where would you like to go? here are your options below")

    for _, v in ipairs(UserOptions) do -- Prints all the options that the user can choose
        print(v)
    end

    UserChoice = io.read()

    Iterate = 1

    while Iterate >= #UserOptions do
        if UserOptions[Iterate] == UserChoice then
            print("Option found")
            break
        end
    end -- FIX THIS

end

StartMenu()