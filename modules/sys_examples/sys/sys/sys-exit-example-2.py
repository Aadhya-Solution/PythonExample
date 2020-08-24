# File: sys-exit-example-2.py
'''
It may not be obvious, but sys.exit doesn’t exit at once. 
Instead, it raises a SystemExit exception. 
This means that you can trap calls to sys.exit in your main program
'''
import sys

print "hello"

try:
    sys.exit(1)
except SystemExit:
    pass

print "there"

## hello
## there
