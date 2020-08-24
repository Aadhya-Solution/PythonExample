'''
The getrefcount function returns the reference
count for a given object
that is, the number of places
where this variable is used.
Python keeps
track of this value, and when it drops to zero,
 the object is destroyed.
'''

# File: sys-getrefcount-example-1.py

import sys

variable = 1234

print sys.getrefcount(0)
print sys.getrefcount(variable)

print sys.getrefcount(None)
'''
50
3
192
'''
