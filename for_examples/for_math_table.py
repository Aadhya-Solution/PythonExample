m=input("Enter a Number:")
for i in range(1,11):
    st=' '
    for j in range(1,m+1):
        p="%dX%d=%d"%(j,i,j*i)
        st=st+" "+p
    print(st)
