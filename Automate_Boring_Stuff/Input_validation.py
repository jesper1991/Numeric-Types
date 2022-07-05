while True:
    print('Enter your age: ')
    age = input()
    try:
        age = int(age)
    except:
        print('Please use numeric digits.')
        continue

    if age < 1:
        print('Enter a positive number.')
        continue
    break
print(f'Your age is {age}.')

# The PyInputPlus Module

import pyinputplus as pyip # Nämna om det så att det går snabbare att skriva
response = pyip.inputInt(prompt='Enter a number: ')
print(response)


# The min, max, greaterThan, and lessThan Keyword Arguments
# The inputNum(), inputInt(), and inputFloat() functions, which accept int and f
# loat numbers, also have min, max, greaterThan, and lessThan keyword arguments for
# specifying a range of valid values. 

response = pyip.inputNum(prompt='Enter num ', min=4) # "Number must be at minimum 4"
response = pyip.inputNum(prompt='Enter a number ',greaterThan=4) # "Number must be greater than 4"
response = pyip.inputNum('>', min=4, lessThan=6)

# Om man vill göra input optinal, använd blank.
response = pyip.inputNum(blank=True)

# The limit, timeout, and default Keyword Arguments
response = pyip.inputNum(prompt='Enter a number, limit = 2: ',limit=2, default = 'N/A')
response = pyip.inputNum(prompt = 'Enter a number in 10 seconds: ',timeout=10)

# Passing a Custom Validation Function to inputCustom()
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbers):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' % (sum(numbersList)))
    return int(numbers)

response = pyip.inputCustom(addsUpToTen)

