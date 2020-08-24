import random
n=input("Enter N:")
l=[]
c=random.randrange(10,100)
print "Selected Base :%d"%(c)
wflag=True
while wflag:
    f=True
    i=2
    while i<=c-1:
        if c%i==0:
            f=False
        i=i+1
    if f:
        l.append(c)
    c=c+1
    if len(l)==n:
        wflag=False

print "Prime Numbers:",l
for i in l:
    print i