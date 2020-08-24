n,m=input('Enter n and m :')
while n<=m:
    c=2
    while c<=n-1:
        if n%c==0:
            break
        c=c+1
    else:
        print "Prime",n
    n=n+1
