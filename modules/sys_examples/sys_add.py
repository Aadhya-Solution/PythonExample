import sys

def add(a,b):
    s=a+b
    return s

print "Script",sys.argv#  file name
if len(sys.argv)>1:
    for i in sys.argv[1:]:
        print i
if sys.argv[1]=='add':
    print "****"
    a=int(sys.argv[2])
    b=int(sys.argv[3])
    s=add(a,b)
    print "%d +%d=%d"%(a,b,s)