# File: sys-path-example-1.py
'''
The path list contains a list of directory
names where Python looks
for extension modules
(Python source modules, compiled modules,
 or binary extensions)
'''
import sys

print "path has", len(sys.path), "members"

# add the sample directory to the path
sys.path.insert(0, "C:\Users\admin\PycharmProjects\pythonExamples\shashi")
import samples

# nuke the path
sys.path = []
import random # oops!

## path has 7 members
## this is the sample module!
## Traceback (innermost last):
##   File "sys-path-example-1.py", line 11, in ?
##     import random # oops!
## ImportError: No module named random
