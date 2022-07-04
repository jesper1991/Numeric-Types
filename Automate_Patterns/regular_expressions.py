# Finding Patterns of Text with Regular Expressions - "regexes"

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




