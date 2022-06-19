
from traceback import print_tb


def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you")

say_hello()

def say_hello(name='Default'):
    print(f'Hello {name}')

say_hello() # Om tomt = 'Default', annars det som är angivet i parentes.

# Function with return

def add_num(num1,num2):
    return num1+num2

sum = add_num(1,2)


def print_result(a,b): # No value returned, just printed.
    print(a+b)

def return_result(a,b): # Value returned and can be stored.
    return a+b

result = return_result(10,30)
result


def say_hello(name='Default'): # If argument not provided = name blir Default
    print(f"Hello {name}")

say_hello("Jesper")

def add_num(num1,num2):
    return num1 + num2

result = add_num(2,3)

def is_even(num1):
    return num1 % 2 == 0 # Returns boolean True or False

is_even(3)

# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

def even_list(num_list):
    # Return all the even numbers in a list
    # Placeholder variables
    evens = []

    for x in num_list:
        if x % 2 == 0:
            evens.append(x)
            
        else:
            pass
        
    return evens # Först efter hela forloopen ska return false kallas. Beginner mistake.

even_list([1,4,3,2,5,67]) # = [4, 2]



    

