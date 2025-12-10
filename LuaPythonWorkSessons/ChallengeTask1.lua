VowelsList = {
    "a",
    "e",
    "i",
    "o",
    "u",
}

Variable = "asfaus"

function CountVowels(VariableInput, TableList)
    for _, Vowel in ipairs(TableList) do
        for VowelFound in Variable:gmatch(Vowel) do
            print(VowelFound.." is a variable")
        end
    end
end

CountVowels(Variable, VowelsList)