# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
# if both numbers are even, but returns the greater if one or both numbers are odd

def myfunc(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1,num2)
    elif num1 %2 != 0 or num2 % 2 != 0:
        return max(num1,num2)

myfunc(2,5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns 
# True if both words begin with same letter

def myfunc(str1,str2):
    lista = []
    listb = []

    for char in str1:
        lista.append(char)
    for char in str2:
        listb.append(char)

    if lista[0] == listb[0]:
        return True
    return False

myfunc('Jesper', 'Akerberg')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
# or if one of the integers is 20. If not, return False

def myfunc(int1,int2):
    if int1 + int2 == 20 or int1 * int2 == 20 or int1 - int2 == 20:
        return True
    return False

myfunc(20,1)

# OLD MACDONALD: Write a function that capitalizes the first 
# and fourth letters of a name

def myfunc(name):
    namelist = []
    for char in name:
        namelist.append(char)
    newname = namelist[0:3]+namelist[3:6]
    return newname

myfunc('jesper')

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def myfunc(sentence):
    mylist = [sentence.split()]
    newsent = mylist[1:2]


    return newsent

myfunc('Hey There')



