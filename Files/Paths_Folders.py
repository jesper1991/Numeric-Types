from pathlib import Path
import os

Path('spam', 'bacon', 'eggs')
str(Path('spam','bacon','eggs'))

# Using the / Operator to Join Paths after already created with Path().

Path('spam') / 'bacon' / 'eggs' # = spam+ bacon + eggs - spam\\bacon\\eggs
Path('spam') / Path('bacon/eggs') # samma
Path('spam') / Path('bacon','eggs') # samma

homeFolder = Path('C:/Users/Al')
subFolder = Path('spam')
str(homeFolder / subFolder) # = C:\\Users\\Al\\Spam

# Current and changing directory
Path.cwd()
os.chdir('C:\\Code\\Numeric-Types')
Path.cwd()

# Home Directory
Path.home()

# Creating New Folders Using the os.makedirs() Function
os.makedirs('C:\\delicious\\walnut\\waffles') # Skapar alla dessa folders

# To make a directory from a Path object, call the mkdir() method. 
# For example, this code will create a spam folder under the home folder on my computer:

Path(r'C:\Users\Jesper\spam').mkdir() # Note that mkdir() can only make one directory at a time.

# Handling Absolute and Relative Paths

Path.cwd()
Path.cwd().is_absolute() # True

Path('spam/bacon/eggs').is_absolute() # False

# Get absolute path from a relative path
Path('my/relative/path')
Path.cwd() / Path('my/relative/path')
Path.home() / Path('my/relative/path')

os.path.abspath('.\\Scripts')
os.path.isabs('.') # False
os.path.isabs(os.path.abspath('.'))

# Getting the Parts of a File Path
p = Path('C:/Users/Jesper/spam.txt')
p.anchor
p.parent # Path
p.name # File name + extension
p.stem # File name
p.suffix # Extension
p.drive # C:

# Finding File Sizes and Folder Contents
os.path.getsize('C:\\Windows\\system32')
os.listdir('C:\\Windows\\System32')

# Checking Path Validity
p = Path('C:/Users/Jesper')
p.exists() # True
p.is_file() # False
p.is_dir() # True

