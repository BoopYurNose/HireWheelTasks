'''
Challenge Overview
Convert a phrase into a URL-friendly slug.

Prompt the user for a phrase or title.
Lowercase the text and remove punctuation/symbols (keep letters, numbers, and spaces).
Replace spaces with hyphens and collapse multiple hyphens.
Handle empty or all-symbol input with a friendly message.
'''
def UrlConverter(Phrase):
    ConvertedUrl = []
    for Character in Phrase:
        if " " in Character:
            ConvertedUrl.append("-")
        if Character.isalnum():
            ConvertedUrl.append("".join(Character))
            
    FinalPhrase = ("".join(ConvertedUrl))
    FinalPhrase = FinalPhrase.lower()
    return FinalPhrase



def UserStart():
    print("Welcome to the URL friendly slug converter!")
    UserPhrase = input("Please type in your phrase:")
    
    if not UserPhrase.strip():
        print("Try again, you need to have an input")
        UserStart()
        return
    elif UserPhrase.isdigit():
        print("Try again, you need to have letters too")
        UserStart()
        return
    print(UrlConverter(UserPhrase))
    
        
UserStart()
