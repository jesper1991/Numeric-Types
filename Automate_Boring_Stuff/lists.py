spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0]
spam[0][1]
spam[1][4]  # The first index dictates which list value to use, 
            # and the second indicates the value within the list value.
spam[-1]    # Negativ index är möjligt, börjar då bakifrån.

# Slicing a list
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1:4]
spam[2:]

# Getting length of list
len(spam) # om listan innehåller flera listor visas antal listor
len(spam[1]) # För att få länge av lista nr 2 i spam.






