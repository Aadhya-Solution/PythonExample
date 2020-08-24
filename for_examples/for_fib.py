
def fib_gen(n):
#fib 0,1,1,2,3,5...
    l=[0,1]
    for i in range(2,n):
        fib=l[i-1]+l[i-2]
        l.append(fib)
    return l
while True:
    try:
        n=input("Enter Number")
        l = fib_gen(int(n))
        print("Fib List:{}".format(l))
        break
    except ValueError:
        print("Provide proper int value")


