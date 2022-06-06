# *args and **kwargs

def myfunc(a,b,c=0,d=0):
    # Returns 5% of the sum of a and b
    return sum((a,b,c,d)) * 0.05

myfunc(40,60)

# *args - unlimited, put in tuple
def myfunc(*args):
    return sum(args) * 0.05

myfunc(40,60,100)

def myfunc(*args):
    for item in args:
        print(item)

myfunc(40,60,100,1,34)

# Keyworded arguments, **kwargs

def myfunc(**kwargs): # Keyword args, created dictionary.
    if 'fruit' in kwargs:
        print(f'My choice is: {kwargs["fruit"]}')
    else:
        print('I did not find any fruit here.')

myfunc(fruit = 'apple', veggie ='lettuce')

# Combo

def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print(f'I would like {args[0]} {kwargs["food"]}')

myfunc(10,20,30, fruit = 'orange', food = 'eggs', animal = 'dog')