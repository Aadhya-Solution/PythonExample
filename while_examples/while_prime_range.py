c=1
while c<=20:
    f=True
    i=2
    while i<=c-1:
        if c%i==0:
            f=False
        i=i+1
    if f:
        print "prime:",c
    c=c+1
