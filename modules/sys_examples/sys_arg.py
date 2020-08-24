
import sys
'''
print sys.argv[0]
if len(sys.argv)>1:
    for arg in sys.argv[1:]:
        print arg
else:
    print "No arguments"
   
    
print sys.path
sample="sample"
sys.path.insert(0,sample)
print sys.path
#import sample
sys.path=[]
print "===",sys.path
import random

a=10
str1="hello"
print sys.getrefcount(a)
print sys.getrefcount(str1)
print sys.getrefcount(0)
print sys.getrefcount(None)


print "Hello"
sys.exit()
print "Hi"
'''
def exitfun():
    print "Hello Bye"
    
sys.exitfunc = exitfun

print "Shashi"
sys.exit(1)
print "Never came here  "