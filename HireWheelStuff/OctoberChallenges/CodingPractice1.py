#PSEUDO CODE
'''
define function PalidromeChecker Arguement it takes in is UserInput (UserInput)
us the string method .isalpha() on UserInput to check if every character in the string is a valid character
I will nest the .isalpha() string method in for loop where in that for loop it will be nested inside a if statement
this for loop will iterate thru each individual character and for each individual character it will use the string method .isalpha() to check if it's a valid character
if it is it'll display that specific character and notify the user that it is a valid character
if it is not a valid character it'll tell the user that specific character and notify them that it is not a valid character tell the user to try again and promptly exit the function

Side Note:
I know it's not necessary to use a for loop to iterate through each character in the UserInput text as the string method .isalpha() already does that and I could just do
an if statement to check if .isalpha() equal to true (meaning if it's true every character in the userInput is a valid character) but I thought it would be cooler to actually
let the user know of all the valid characters in their text input and let them know if one of them is not a valid input. Either way works fine but I prefer it letting the user
know what characters were valid and what weren't (if any weren't at all) 


if all is successful, I will create a new variable called ReversedString and equal it to the UserInput text except the UserInput text is sliced basically I'm making ReversedString equal to reversed UserInput text
then it will do a if statement checking if UserText and ReversedString - (UserText but reversed) are equal to eachother
if they are equal to eachother it will notify the user that their text input is indeed a palindrome if they are not equal to eachother it will notify the user that the text is not a palidrome
'''

def PalindromeCheck(UserText):
    

    for Word in UserText:
        if Word.isalpha():
            print(f"{Word} is a valid character ")
        else:
            print(f"{Word} is not a valid character in your text input. Please try again.")
            return
    
    UserText = UserText.lower()
        
    
    ReversedText = UserText[::-1]
    if UserText == ReversedText:
        print(f"Your word {UserText} is a palindrome")
    else:
        print(f"Your word {UserText} is not a palindrome")
    

UserInput = input("Check if a word is a Palidrome. Please type in your text: ")
PalindromeCheck(UserInput)