# Range function


for num in range(2,10,2): # printa från 2-10(up to 10) med 2 steps = jämna tal
    print(num)


# Enumerat
index_count = 0

for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1

# Enumerate function
word = 'abcde'

for index,letter in enumerate(word):
    print(index,letter)

# Zip function

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]

#iterate
for item in zip(mylist1,mylist2,mylist3):
    print(item)
#bara få fram lista
list(zip(mylist1,mylist2,mylist3))

# in-operator

'x' in [1,2,3]
'x' in ['x','y','z']
'a' in 'a world'
d = {'mykey':345}
345 in d.values()

# Useful math operators, min max, random

mylist = [10,20,30,40,100]
min(mylist)
max(mylist)

from random import shuffle
import re
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

import random
myrand = random.randint(0,100)
print(myrand)

# Input
result = int(input('Enter a number here: ')) # Om inte int direkt kan du casta enl. nedan
int(result)




