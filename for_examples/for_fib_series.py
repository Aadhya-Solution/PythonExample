num1=input("Enter some value:")
num2=input("Enter some value:")
l1=[]
l=[0,1]
for i in range(2,num2):
    l.append(l[i-1]+l[i-2])
    if l[i]>=num1 and l[i]<=num2:
        l1.append(l[i])
print("Fib Sieries is ",l)
print("Fib b/w",num1,"&",num2,"==",l1)
#0,1,1,2,3,5,8,13,21...