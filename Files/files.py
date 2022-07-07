# Opening Files with the open() Function

from pathlib import Path
import shelve

# Öppna med Path, fungerar i Python 3.6+
helloFile = open(Path.home() / 'hello.txt')

# Öppna med string
helloFile = open('C:\\Users\\Jesper\\hello.txt')

# Reading the Contents of Files
helloContent = helloFile.read()
helloContent

# Separate lines to list
sonnetFile = open(Path.home() / 'sonnet29.txt')
sonnetFile.readlines()

# Writing to Files, w = overwrites from scratch, a = appends

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello World!\n')
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()

baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

# Saving Variables with the shelve Module

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka','Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
shelfFile['cats']
shelfFile.close()

# Just like dictionaries, shelf values have keys() and values() methods that will
# return list-like values of the keys and values in the shelf. 

shelfFile = shelve.open('mydata')
list(shelfFile.keys())
list(shelfFile.values())
shelfFile.close()

# Saving Variables with the pprint.pformat() Function
import pprint
cats = [{'name': 'zophie', 'desc': 'chubby'}, {'name':'pooka', 'desc': 'fluffy'}]
pprint.pformat(cats)
fileObj = open('myCats.py', 'w')
fileObj.write('cats = ' + pprint.pformat(cats) + '\n')
fileObj.close()

import myCats
myCats.cats
myCats.cats[0]
myCats.cats[0]['name']




