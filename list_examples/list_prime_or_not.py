n=input("Enter n:")
f=True
for i in range(2,n):
    if n%i==0:
        f=False
if f:
    print "Given Number is Prime"
else:
    print "Given number not a prime"