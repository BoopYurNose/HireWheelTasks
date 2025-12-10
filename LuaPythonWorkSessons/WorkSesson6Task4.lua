UserLimitTries = 3
UserAttempts = 0 -- Amount of User Attempts

SecretWord = "amelia"

SecretReverseWord = string.reverse(SecretWord)

print("Hello welcome your goal is to guess what this work is it will be shown to you except.. It will be reversed. \n your hint is that it is a name")
print("Okay here is your word: "..SecretReverseWord)

while UserAttempts < UserLimitTries do
    print("Try to guess the secret word! type it!")
    UserGuess = io.read()
    if UserGuess ~= SecretWord then
        UserAttempts = UserAttempts + 1
        print("no good try but try again you have "..UserLimitTries - UserAttempts.." attempts left")
    elseif UserGuess == SecretWord then
        print("Good job you guessed it it was amelia great job!!")
        break
    end
end

if UserGuess ~= SecretWord then
    print("You ran out of guesses you did not guess the name it was amalia good try")
end