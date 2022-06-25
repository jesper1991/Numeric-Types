
# Dictionaries = key value pairs. Unordered.

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

myCat['size'] # index

f'My cat has {myCat["color"]} fur' # F-string
'My cat has ' + myCat['color'] + ' fur.' # Concatenation

# Birthday data program

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input
    if name == '':
        break

    if name in birthdays:
        print(f'{birthdays[name]} is the brithday of {name}')
    else:
        print(f'I do not have birthday information for {name}')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

# The keys(), values(), and items() Methods - dict_keys, dict_values, and dict_items

spam = {'color': 'red', 'age': 42}
for v in spam.values(): # Bara värden
    print(v)

for k in spam.keys():   # Bara keys
    print(k)

for i in spam.items():  # Båda - blir tuple
    print(i)

list(spam.keys())
list(spam.values())

for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Checking Whether a Key or Value Exists in a Dictionary
spam = {'name':'Zophie', 'age': 7}
'name' in spam.keys() # True
'Zophie' in spam.values() # True
'color' not in spam.keys() # True
'color' in spam # False

# The get() Method
picnicItems = {'apples':5, 'cups':2}
print(f'I am bringing {str(picnicItems.get("cups",0))} cups') # 0 = default value
print(f'I am bringing {str(picnicItems.get("eggs",0))} eggs') # 0 blir värdet då eggs inte finns.

# The setdefault() Method
# You’ll often have to set a value in a dictionary for a certain 
# key only if that key does not already have a value. 

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'

# setdefault method:
spam.setdefault('color','black') # Om color redan finns returneras value
# T.ex. skulle nu spam.setdefault('color':'white') returnera black

# Short program that counts the number of occurrences of each letter in a string

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for char in message:
    count.setdefault(char,0)
    count[char] = count[char] + 1
print(count)