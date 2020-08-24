n1=input("Enter the n1 value:")
n2=input("Enter the n2 value:")
for num in range(n1,n2):#[10,11,12
    flag=True
    for i in range(2,num): #[2,3,4,...9]
        if num % i == 0:
            break
    else:
        print("Number is prime",num)