# File: os-example-4.py

import os

# where are we?
cwd = os.getcwd()
print "1>>>", cwd

# go down
os.chdir("samples")
print "2>> Change dir", os.getcwd()

# go back up
os.chdir(os.pardir)
print "3>> comping back:", os.getcwd()

## 1 /ematter/librarybook
## 2 /ematter/librarybook/samples
## 3 /ematter/librarybook
