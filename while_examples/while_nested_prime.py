n,m=input("Enter N,M:")
while n<=m:
    c=2
    f=True
    while c<=n-1:
        if n%c==0:
            f=False
        c=c+1
    if f:
        print "Prime",n
    n=n+1
