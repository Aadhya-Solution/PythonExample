N# !/usr/bin/python
import os, sys

# listing directories
print "The dir is: %s" %os.listdir(os.getcwd())

# removing
os.removedirs("abdTest")

# listing directories after removing directory
print "The dir after removal is:" %os.listdir(os.getcwd())

'''
The method removedirs() removes dirs recursively.

If the leaf directory is succesfully removed, removedirs tries to successively
remove every parent directory displayed in pat

The dir is:
[  'a1.txt','resume.doc','a3.py','tutorialsdir','amrood.admin' ]

The dir after removal is:
[  'a1.txt','resume.doc','a3.py','amrood.admin' ]
'''