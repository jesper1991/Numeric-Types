import imp


def hello(name):
    print('Hello ' + name)

hello('Jesper')


# 8-ball

import random

def getAnswer(answerNumber):

    
    if answerNumber == 1:
        return 'It is uncertain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1,9)
fortune = getAnswer(r) # Kan köra random.randint(1,9) här
print(fortune)

# print(getAnswer(random.randint(1,9))) mer förkortat

# Keyword arguments för t.ex. print function

print('Hello', end='')
print('World')

print('cats', 'dogs', 'mice', sep=',') # Specifierad separator



