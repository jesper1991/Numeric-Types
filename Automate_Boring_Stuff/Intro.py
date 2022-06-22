print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.') # Gör om myage till int och räknar ut sedan till string.

while True: # Infinite loop
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break # Breaks out of loop
print('Thank you!')

# Program som frågar efter username och pw, med continue och break.
# Continue behövs för att fortsätta med första steget tills rätt.

while True:
    print('Who are you?')
    name = input()
    if name != 'Jesper':
        continue
    print('Hello Jesper, what is the password?')
    password = input()
    if password == 'peppe':
        break
print('Access granted.')

# For loop

print('My name is')
for x in range (5):
    print(f'Jesper Five Times ({str(x)})')

# En till
total = 0
for num in range (101):
    total = total+num
print(total)

# En till
for i in range(5, -1, -1):
    print(i)

# Importing modules

import random
for i in range(5):
    print(random.randint(1, 10))

import sys, os, math  # Kan importera flera samtidigt

# Ending a program early with sys.exit() function

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print(f'You typed {response}.')
    break


spam = 3
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

for x in range(1, 11):
    print(x)

x = 1
while x < 11:
    print(x)
    x = x + 1

