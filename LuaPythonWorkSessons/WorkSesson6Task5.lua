-- Simple Calculator

function Addition(Number1, Number2)
    local Answer = Number1 + Number2
    print("Your answer is "..Answer)
end

function Subtraction(Number1, Number2)
    local Answer = Number1 - Number2
    print("Your answer is "..Answer)
end

function Division(Number1, Number2)
    local Answer = Number1 / Number2
    print("Your answer is "..Answer)
end

function Multiplication(Number1, Number2)
    local Answer = Number1 * Number2
    print("Your answer is "..Answer)
end

local FirstUserNumber

while type(FirstUserNumber) ~= "number" do
    print("Hello welcome to the calculator please type in your first number input")
    FirstUserNumber = io.read()
    if tonumber(FirstUserNumber) ~= nil then
        print("This works! \n")
        FirstUserNumber = tonumber(FirstUserNumber)
    end
end

local SecondUserInput

while type(SecondUserInput) ~= "number" do
    print("Now type in your second number input")
   SecondUserInput = io.read()
   if tonumber(SecondUserInput) ~= nil then
    print("Alright good job! \n")
    SecondUserInput = tonumber(SecondUserInput)
   end
end

AcceptableOperators = {
    "+",
    "-",
    "/",
    "*"
}

local OperatorWorking = false

local OperatorInput

while OperatorWorking == false do
    print("Now put in a operator of either + - / *")
    OperatorInput = io.read()
    for i = 1, #AcceptableOperators do
        if OperatorInput == AcceptableOperators[i] then
            print("This works")
            OperatorWorking = true
            break
        end
    end
end

if OperatorInput == "+" then
    Addition(FirstUserNumber, SecondUserInput)
elseif OperatorInput == "-" then
    Subtraction(FirstUserNumber, SecondUserInput)
elseif OperatorInput == "/" then
    Division(FirstUserNumber, SecondUserInput)
elseif OperatorInput == "*" then
    Multiplication(FirstUserNumber, SecondUserInput)
end
