import sys

def collatz(num):
    if num % 2 == 0:
        print(num//2)
        return num//2
    elif num % 2 != 0:
        print(num * 3 + 1)
        return num * 3 + 1

try:
    answer = int(input('Type a number: '))
    while answer != 1:
        answer = collatz(answer)
except ValueError:
    sys.exit('Not a number. Shutting Down.')
        
        
