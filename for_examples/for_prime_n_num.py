n1=input("Enter the n1 value:")
for num in range(1,n1):#[10,11,12
    flag=True
    for i in range(2,num): #[2,3,4,...9]
        if num % i == 0:
            flag=False
            break
    if flag:
        print("Number is prime",num)