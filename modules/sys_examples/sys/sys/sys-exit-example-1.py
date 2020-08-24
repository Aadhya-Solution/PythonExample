# File: sys-exit-example-1.py
'''
Exiting the program #

When you reach the end of the main program, 
the interpreter is automatically terminated. 
If you need to exit in midflight, you can call the sys.exit function instead. 
This function takes an optional integer value, which is returned to the calling program
'''
import sys

print "hello"

sys.exit(1)

print "there"

## hello
