# Converting Types with the list() and tuple() Functions

tuple(['cat','dog','moose']) # Visar tupleversion av listan som anges

# Gör en tuplekopia av lista
mylist = ['cat','dog']
mytuple = tuple(mylist)
mytuple

# Gör listkopia av tuple, bra om man behöver kunna ändra värden
mylist = list(mytuple)
mylist

