n,m=input("Enter N,M:")
for i in range(n,m+1):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
    if flag:
        print("Prime:",i)
