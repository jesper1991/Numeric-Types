spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
spam[0][1]
spam[1][4]  # The first index dictates which list value to use, 
            # and the second indicates the value within the list value.
spam[-1]    # Negativ index är möjligt, börjar då bakifrån.

# Slicing a list
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1:4]
spam[2:]

# Getting length of list
len(spam) # om listan innehåller flera listor visas antal listor
len(spam[1]) # För att få länge av lista nr 2 i spam.

# Changing values
spam[1] = 'butterfly'

# Concatenation and List replication

spam = [1,2,3] + ['A','B', 'C']
['X','Y','Z'] * 3

# Removing values with del
spam = [1,2,3,4]
del spam[2]


# Cats program with list

catNames = []

while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.): ')
    name = input()
    if name == '':
        break
    catNames.append(name)
print('The cat names are:')
for x in catNames:
    print('  ' + x)


# For loops with list - iterate over indexes of a list
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for x in range(len(supplies)):
    print('Index '+ str(x) + ' in supplies is: ' + supplies[x])

# in and not in operators - boolean values

'howdy' in ['hello', 'hi', 'heyas', 'howdy'] # True
spam = ['hello','hi','howdy','heyas']
'cat' in spam # False

myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name: ')
name = input()
if name not in myPets:
    print(f'I do not have a pet named {name}')
else:
    print(f'{name} is my pet.')

# Multiple assignment trick
cat = ['Fat', 'Gray', 'Loud']
size,color,disposition = cat # assign variables to list index - Size = Fat etc.

# Enumerate with list instead of for loop to get index and item

supplies = ['pens', 'staplers' ,'flamethrowers' ,'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is ' + item)

# Using the random.choice() and random.shuffle() Functions with Lists

import random
pets = ['Dog', 'Cat', 'Moose']
random.choice(pets)

import random
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
people

# Augmented assignment operators

# spam += 1      spam = spam + 1

# spam -= 1      spam = spam - 1

# spam *= 1      spam = spam * 1

# spam /= 1      spam = spam / 1

# spam %= 1      spam = spam % 1

# Finding a Value in a List with the index() Method. Will not return duplicates, only first match.

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello')

# Adding Values to Lists with the append() and insert() Methods

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam

# Removing Values from Lists with the remove() Method. Tar bara bort första träffen.
spam = ['cat', 'dog', 'bat']
spam.remove('cat')
spam

# The del statement is good to use when you know the index of the value you want to 
# remove from the list. The remove() method is useful when you know the value 
# you want to remove from the list.

# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam

# Reverse sorting
spam.sort(reverse=True)
spam

# sort() uses “ASCIIbetical order” rather than actual alphabetical order 
# for sorting strings. This means uppercase letters come before lowercase letters. 
# Therefore, the lowercase a is sorted so that it comes after the uppercase Z.

# If you need to sort the values in regular alphabetical order, 
# pass str.lower for the key keyword argument in the sort() method call.

spam = ['Alice', 'alice', 'Bob', 'badgers']
spam.sort(key=str.lower)
spam

