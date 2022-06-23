# Sequence Data Types

name = 'Zophie'
name[0]         # Z
name[0:4]       # Zoph
'Zo' in name    # = True
'z' in name     # = False
for char in name:
    print('***' + char + '***')

# Can't change value of char in string. Need to slice and concatenate.

name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]
newName         # Zophie the cat

# Identity and the id() Function

id('howdy')
id(name)
