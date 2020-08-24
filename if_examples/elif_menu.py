line="="*50
head="Arthematic Operation".center(50)
menu='''
     1.ADD
     2.SUB
     3.MUL
     4.DIV
     5.EXIT
     '''
print line
print head
print line
print menu
print line
opt=input("Enter Opt:")
a=input("Enter A:")
b=input("Enter B:")
if opt==1:
    t=a+b
    print "%d+%d=%d"%(a,b,t)
elif opt==2:
    s=a-b
    print "%d-%d=%d"%(a,b,s)
elif opt==3:
    p=a*b
    print "%dX%d=%d"%(a,b,p)
elif opt==4:
    d=a/b
    print "%d/%d=%d"%(a,b,d)
else:
    print "Bye"



