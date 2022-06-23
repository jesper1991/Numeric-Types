# Om man inte vill ändra i originallistan t.ex kan man använda copy.

import copy
spam = ['A','B','C','D']
id(spam)
cheese = copy.copy(spam)
id(cheese)

# Cheese är nu en kopia av spam, men inte samma ID. Ändringar görs då endast på Cheese.

# copy.deepcopy() om listan innehåller listor.

