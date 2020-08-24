a=int(raw_input("Enter a valu"))
b=int(raw_input("Enter b valu"))
c=int(raw_input("Enter c valu"))

if a<b and b<c:
    print "C is big"
elif a>b and a>c:
    print "A is big"
else:
    print "B is big"


if a<b:
   if b<c:
       print "C is big"
   else:
       print "B is big"
else:
   if a>c:
       print "A is Big"
   else:
       print "C is big"
	
