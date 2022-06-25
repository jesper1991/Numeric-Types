# Escape character
from platform import python_branch


spam = 'Say hi to bob\'s mother.'
spam
# \'    Single quote
# \"    Double quote
# \t    Tab
# \n    Newline (line break)
# \\    Backslash

print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw Strings - Ignores escape characters
print(r'That is Carol\'s cat.') # Includes \

# Multiline Strings with Triple Quotes, istället för \n osv. Programmet tolkar som det skrivs.

print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,

Bob''')

# Multiline Comments

def spam():
    """
    This is a multiline comment to help
    explain what the spam() function does.
    """
    print('Hello!')

spam() # = 'Hello!'

