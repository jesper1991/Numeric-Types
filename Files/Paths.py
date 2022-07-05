from pathlib import Path
Path('spam', 'bacon', 'eggs')
str(Path('spam','bacon','eggs'))

# Using the / Operator to Join Paths after already created with Path().

Path('spam') / 'bacon' / 'eggs' # = spam+ bacon + eggs - spam\\bacon\\eggs
Path('spam') / Path('bacon/eggs') # samma
Path('spam') / Path('bacon','eggs') # samma





