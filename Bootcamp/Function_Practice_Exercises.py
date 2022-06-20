
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
from unittest import result


def lesser_of_two_evens(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1,num2)
    else:
        return max(num1,num2)
    



lesser_of_two_evens(4,2)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter

def same_letter(str1):
    
    words = str1.lower().split()
    if words[0][0] == words[1][0]:
        return True

    else:
        pass

    return False

same_letter("animal crackers")
same_letter("Lnimal Lrackers")

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(num1,num2):

    return (num1+num2) == 20 or num1 == 20 or num2 == 20 or num1 * num2 == 20 or num1 - num2 == 20 # Returns bool value True or False


makes_twenty(2,3)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# old_macdonald('macdonald') --> MacDonald

# Klarade det inte

def capitalize(name):
    index = 0
    result = ''

    for letter in name:
        if index == 0 or 3:
            result += letter.upper()
            index +=1
        else:
            index += 1

    return result

capitalize('jesper')

# Lösning via slicing och uppercase

def old_macdonald(name):

    first_letter = name[0]
    inbetween = name[1:3]
    fourth_letter = name[3]
    rest = name[4:]
# Concatenate together again
    return first_letter.upper() + inbetween + fourth_letter.upper() + rest

old_macdonald('jesper')

# Capitilize method

def old_macdonald(name):
    first_half = name[:3]
    second_half = name[3:]
    
    return first_half.capitalize() + second_half.capitalize()

old_macdonald('jesper')

# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    wordlist = text.split()
    reversed = wordlist[::-1]
    return ' '.join(reversed) # Ersätt 


master_yoda('home am I')
# Join 

# Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return (abs(100-n) <= 10) or (abs(200-n) <= 10)


almost_there(111)

    
def blackjack(a,b,c):
    if sum([a,b,c]) <= 21:
        return sum([a,b,c])
    elif 11 in [a,b,c] and sum ([a,b,c]) <= 31:
        return sum([a,b,c])-10
    else:
        return "BUST"




