
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

