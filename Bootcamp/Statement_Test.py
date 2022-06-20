# Use for, .split(), and if to create a Statement that will 
# print out words that start with 's':

st = 'Print only the words that start with s in this sentance'

for word in st.split():
    if word[0].lower() =='s':
        print(word)
    else:
        pass


# Use range() to print all the even numbers frm 0 to 10.

for num in range(0,11):
    if num % 2 == 0:
        print(num)

# Rätt
for num in range(0,11,2):
    print(num)


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

mylist = [x for x in range(1,51) if x % 3 == 0]
print(mylist)

# Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
mylist = st.split()

# Fel, använde inte len så det blir inte int...
for x in mylist:
    if x % 2 == 0:
        print(x)
    else:
        pass

# Rätt:
st = 'Print every word in this sentence that has an even number of letters'

for x in st.split():
    if len(x) % 2 == 0:
        print(x+ ' is even!')


# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

# Mitt
for num in range(1,101):
    if num % 3 == 0:
        print("Fizz")
    if num % 5 == 0:
        print("Buzz")
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    else:
        print(num)

# Rätt:
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Use list comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

[word[0] for word in st.split()]