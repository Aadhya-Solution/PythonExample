# File: sys-argv-example-1.py
'''
The argv list contains the arguments passed to the script,
 when the interpreter was started. 
 The first item contains the name of the script itself.
'''
import sys
print "====>",sys.argv
print "script name is", sys.argv[0]

if len(sys.argv) > 1:
    print "there are", len(sys.argv)-1, "arguments:"
    for arg in sys.argv[1:]:
        print arg
else:
    print "there are no arguments!"

## script name is sys-argv-example-1.py
## there are no arguments!
