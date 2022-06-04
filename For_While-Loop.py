mylist = [1,2,3,4,5,6,7,8,9,10]

for x in mylist:
    print(x)


for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f"Odd number: {num}")


list_sum = 0

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

# Strings
mystring = 'Hello World'

for _ in mystring:
    print(_)

# Tuple
tup = (1,2,3)
for item in tup:
    print(item)

# Tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]

len(mylist) # 4

for a,b in mylist:
    print(a)
    print(b)

mylist = [(1,2,3), (5,6,7),(8,9,10)]

for a,b,c in mylist:
    print((a),(b),(c))

# Dictionary

d = {'k1':1, 'k2':2,'k3':3}

for _ in d.items(): # Blir bara keys
    print(_)

for key,value in d.items(): # "Unpacking", printa bara values
    print(value)

# WHILE

x = 6

while x < 5:
    print(f"The current value of x is: {x} ")
    x += 1

else:
    print("X is not less than 5")

# break, continue, pass

# pass - Does nothing
x = [1,2,3]

for item in x:
    pass        # Används för att hoppa över tills man vet vad man vill göra. Annars syntax error


# continue - Goes to the top of the closest enclosing loop

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    elif letter == 'm':
        continue
    print(letter) # Blir Sy, continue = hoppa över och gå tillbaka och loopa till nästa

# break - Breaks out of the current closes enclosing loop

mystring = 'Jesper'

for letter in mystring:
    if letter == 'e':
        break
    print(letter) # Slutar efter J då e förekommer.


x = 0

while x < 5:
    if x == 2:
        break
    print(x)
    x += 1


