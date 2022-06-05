
import re


mylist = [1,2,3]
mylist.append(4)
mylist.pop()
mylist

# How to get a list of methods for an object - t.ex. mylist.punkt för att se alla
mylist.insert
help(mylist.insert)

# def keyword

# def name_of_function():

def test():
    '''
    Explain function.
    '''
    print("Hello")

    test() # call function

# Can accept argument

def add_function(num1,num2):
    return num1+num2

result = add_function(1,2)
print(result)