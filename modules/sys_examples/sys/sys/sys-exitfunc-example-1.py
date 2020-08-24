import sys

def hello():
    print "world"
    print "Raghu"

def fun():
    print "Fun"
    print "I am exiting"

sys.exitfunc = fun
print "hello"
hello()
sys.exit()
print "there" # never printed

## hello
## world
