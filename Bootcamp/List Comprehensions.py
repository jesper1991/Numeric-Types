# List comprehensions are a unique way of quickly creating a list with Python

mystring = 'hello'

mylist = []
for letter in mystring:
    mylist.append(letter)

print(mylist)

# List comprehension

mylist = [letter for letter in mystring]
print(mylist)

mylist = [x for x in 'word']
print(mylist)

# Can do operation
mylist = [num**2 for num in range(0,11)]
print(mylist)

# Even numbers
mylist = [x for x in range(0,11) if x%2==0]
print(mylist)

# More complex list comprehension
celcius =[0,10,20,34.5]

fahrenheit = [( (9/5*temp + 32) for temp in celcius)]
print(fahrenheit)

# Normal for-loop
fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))

print(fahrenheit)

# Nested loops 

mylist = []

for x in [2,4,6]:
    for y in [1,10,1000]:
        mylist.append(x*y)

print(mylist)

