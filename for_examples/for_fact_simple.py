num=input("Enter some value to find fact")
fact=1
for i in range(1,num+1):
    fact=fact*i
print("fact of ",num,"is",fact)
print("fact of %d is %d"%(num,fact))