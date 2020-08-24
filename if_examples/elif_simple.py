a=raw_input("Enter A:")
if 'rama' in a:
    print "A is one"
elif a=='two':
    print "A is two"
elif a==3:
    print "A is three"
else:
    print "A is nothing"
flag=True
for i in range(20):
    if i%2==0:
        print i
flag=True
if flag:
    print "Yes i am in"
