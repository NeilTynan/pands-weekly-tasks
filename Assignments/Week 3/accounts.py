# python accounts.py

# Please enter an 10 digit account number:
AccountNo = (input())

def anon_account():
    try:
        # Adjust the account number to replace everything but last four digits with X
        replacements = str.maketrans({"1": "X", "2": "X", "3": "X","4": "X", "5": "X", "6": "X","7": "X", "8": "X", "9": "X"})
        FirstPart = AccountNo[:-4].translate(replacements)
        SecondPart = AccountNo[-4:]
        print(FirstPart+SecondPart)
    except:
        print("Please enter a 10 digit integer")

#  Print out the anonymised account number
anon_account()

# Notes: str.maketrans() function maps characters to their replacements. translate() method applies the mapping to the string.