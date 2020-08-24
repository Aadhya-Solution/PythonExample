import sys
print('--->',len(sys.argv))
for i in range(len(sys.argv)):
    print(i,'-->',type(sys.argv[i]))
if len(sys.argv)==4:
    if sys.argv[1]=='add':
        if sys.argv[2] in [int,float] and sys.argv[3] in [int,float]:
            a,b=eval(sys.argv[2]),eval(sys.argv[3])
            c=a+b
            print( "Sum is ",c)
        else:
            print("Provide proper inputs")
    elif sys.argv[1]=='mul':
        if sys.argv[2] and sys.argv[3]:
            a,b=eval(sys.argv[2]),eval(sys.argv[3])
            c=a*b
            print("Multiplication is ",c)


else:
    print("Provide proper arguments")