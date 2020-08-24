c,m=input("Enter c and M:")
l=[]
while c<=m:
    f=True
    i=2
    while i<=c-1:
        if c%i==0:
            f=False
        i=i+1
    if f:
        l.append(c)
    c=c+1

print "Prime Numbers:",l
for i in l:
    print i