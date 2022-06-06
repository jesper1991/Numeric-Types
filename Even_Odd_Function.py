
# Even odd numbers function

# Check if even
20 % 2 == 0 # True

21 % 2 == 0 # False

def even_check(number):
    return number % 2 == 0

even_check(20) # True
even_check(21) # False


# RETURN TRUE IF ANY NUMBER IS EVEN INSIDE A LIST

def check_even_list(num_list):

    for number in num_list:
        if number % 2 == 0:
            return True
        else:
            pass        # Can't use return False

    return False

check_even_list([1,3,5,7])
check_even_list([1,2,4,7])

# Return values instead of True/False:

def check_even_list(num_list):
    # return all the even numbers in a list
    
    # placeholder variables
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass        # Can't use return False

    return even_numbers

check_even_list([1,2,3,4,5])
check_even_list([1,3,5])