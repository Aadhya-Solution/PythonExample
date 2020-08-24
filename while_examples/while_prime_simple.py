wflag=True
while wflag:
    n=input("Enter N:")
    c=2
    flag=True
    while c<=n-1:
        if n%c==0:
            flag=False
        c=c+1
    if flag:
        print "Given %d is Prime"%(n)
    else:
        print "Given %d is Not Prime"%(n)
    opt=raw_input("Do you want to cont Pree Yes or No")
    if opt.upper().strip() in ['YES','Y']:
        wflag=True
    else:
        wflag=False