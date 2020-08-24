st="""
    1. ADD
    2. SUB
    3. MUL
    4. DIV
    5. Exit
"""
c=1
flag=True
while c<=4:
     print "-"*20
     print st
     print "-" * 20
     a=input('A:')
     b=input("B:")
     opt=input("Opt:")
     if opt==1:
		 s=a+b
		 print "{}+{}={}".format(a,b,s)
     elif opt==2:
         print "{}-{}={}".format(a,b,a-b)
     elif opt==3:
         print "{}X{}={}".format(a, b, a*b)
     elif opt==4:
         print "{}/{}={}".format(a, b, a/b)
     elif opt==5:
         break
     else:
         print "Wrong Opt:"
     c=c+1
     print "==>",c
else:
    print "Arth Opt done"
