print "*"*10
print "1.Add"
print "2. MUl"
print "*"*10
a, b = input("Enter A and B:")
opt=input("Enter OPt:")
if opt ==1:
    c=a+b
    print "{}+{}={}".format(a,b,c)
elif opt ==2:
    c=a*b
    print "%d*%d=%d"%(a,b,c)
else:
    print "Provided wrong Option"
print "*"*10
print "Done"