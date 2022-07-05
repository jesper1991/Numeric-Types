# Finding Patterns of Text with Regular Expressions - "regexes"

from lib2to3.pgen2 import grammar
import re

from pip import main

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex

mo = phoneNumRegex.search('My number is 415-555-4242.') # mo = "Match Objects", common use
print(f'Phone number found: {mo.group()}')


# Grouping with Parentheses

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4343')
mo.group(1)
# The first set of parentheses in a regex string will be group 1. The second set will be group 2.
# Passing 0 or nothing to the group() method will return the entire matched text.

# If you would like to retrieve all the groups at once, use the groups() method—note the plural form for the name.

mo.groups() # = ('415', '555-4343') TUPLE, can use assignment to this, se under.

areaCode, mainNumber = mo.groups()
print(areaCode) # 415
print(mainNumber) # 555-4343

# If you need parenthesis in number?

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
mo.group(1)
mo.group(2)

# Matching Multiple Groups with the Pipe
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
mo1.group()
mo2 = heroRegex.search('Tina Fey')
mo2.group()

# You can also use the pipe to match one of several patterns as part of your regex.
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group(1) # mobile
mo.group() # batmobile

# Optional Matching with the Question Mark

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('Batman')
mo1.group()
mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()

# Using the earlier phone number example, you can make the regex look for phone numbers that do or do not have an area code.

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
mo1.group() # = 415-555-4242

mo2 = phoneRegex.search('My number is 555-4242')
mo2.group() # = 555-4242

# Matching Zero or More with the Star
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()

mo3 = batRegex.search('The Adventures of Batwowowowoman')
mo3.group()

# Matching One or More with the Plus, minst en måste finnas, annars None.
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batman')
type(mo1) # NoneType
mo1 == None # True

# The findall() Method - search() = First, findall() = Alla i en lista av strings.

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegex.findall('415-555-9999 Work: 548-484-4544')

# If there are groups in the regular expression, then findall() will return a list of tuples.
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # = List of tuples

# Character classes

xmasRegex = re.compile(r'\d+\s\w+') # = en eller mer siffra, whitespace, en eller mer bokstav
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

# Making Your Own Character Classes, t.ex. leta vowels.

vowelRegex = re.compile('[AEIOUYaeiouy]')
vowelRegex.findall('Robocop eats baby food. BABY FOOD!')
# By placing a caret character (^) just after the character class’s opening bracket, 
# you can make a negative character class. A negative character class will match 
# all the characters that are not in the character class. 

consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')

# The Caret and Dollar Sign Characters
beginsWithHello = re.compile(r'^Hello') # = Måste börja med Hello
beginsWithHello.search('Hello, world!')

endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('Hello, I am 46')
endsWithNumber.search('Your number is forty two.') == None # = True

wholeStringIsNum = re.compile(r'^\d+$')
wholeStringIsNum.search('12311673')
wholeStringIsNum.search('123ad83') == None

# The Wildcard Character - .  the dot, en punkt för varje tecken innan.

atRegex = re.compile(r'.at') # får inte med brat, men ..at skulle få det.
atRegex.findall('Cat, Rat, Brat, Hat, Sat')

# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
mo.group(1)
mo.group(2)

# Substituting Strings with the sub() Method
namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')









