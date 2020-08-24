s=raw_input("Enter String:")
mtemp=""
l=s.split()
m=len(l)-1
c=0
while c<=m:
    st=l[c]
    rev=""
    m1=len(st)-1
    while m1>=0:
        rev=rev+st[m1]
        m1=m1-1
    mtemp=mtemp+" "+rev
    c=c+1
print "reversed:",mtemp