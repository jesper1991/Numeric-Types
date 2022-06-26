# Escape character
from argparse import ArgumentParser
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

# join() method
', '.join(['cats', 'rats', 'bats']) # = 'cats,rats,bats'

# split() method
'My name is Simon'.split() # = ['My','name','is','Simon']

# partition() method
'Hello, world!'.partition('w') # = ('Hello, ', 'w', 'orld!')
# Multiple assigment trick for partition:
before, sep, after = 'Hello, world!'.partition(' ')
before
sep
after

# Justifying Text with the rjust(), ljust(), and center() Methods

'hello'.rjust(10) # = '     hello'
'Hello'.rjust(20,'*') # = '***************Hello'
'Hello'.ljust(20,'*') # = 'Hello***************'
'Hello'.center(20,'-') # = '-------Hello--------'

def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# Removing Whitespace with the strip(), rstrip(), and lstrip() Methods
spam = '      Hello World'
spam.strip()
spam.lstrip()
spam.rstrip()

# A string argument will specify which characters on the ends should be stripped
spam = 'SpamSpamBaconSpamEggsSpamSpam'
spam.strip('ampS')

# Numeric Values of Characters with the ord() and chr() Functions

ord('A') # = 65
chr(66) # = B

# Bra för jämförelse om A < B t.ex.:
ord('B') > ord('A') # = True

# Copying and Pasting Strings with the pyperclip Module
import pyperclip
pyperclip.copy('Hello, world!')
pyperclip.paste()
