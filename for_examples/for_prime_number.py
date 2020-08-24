num=input("Enter the value:")
flag=False
for i in range(2,num):
    if num % i == 0:
        flag=True
if flag:
    print "Not a prime num:",num
else:
    print "Number is prime",num