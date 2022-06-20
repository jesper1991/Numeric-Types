# 1
def myfunc():
    print("Hello World")

# 2
def myfunc(name):
    print("Hello {}".format(name))

# 3
def myfunc(a):
    if a == True:
        return 'Hello'
    elif a == False:
        return 'Goodbye'

# 4
def myfunc(x,y,z):
    if z == True:
        return x
    elif z == False:
        return y

# 5
def myfunc(num1,num2):
    return num1 + num2

# 6 
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# 7
def is_greater(num1,num2):
    if num1 > num2:
        return True
    else:
        return False

