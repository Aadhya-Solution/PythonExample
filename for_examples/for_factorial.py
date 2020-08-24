num=input("Enter some value to find fact")
fact=1
str_i='*'
for i in range(1,num+1):
    if "*" == str_i:
        str_i=str(i)
    else:
        str_i=str_i+"*"+str(i)
    #print "-->",str_i
    fact=fact*i

print("Fact(%s)=%s=%s"%(str(num),str_i,fact))
print("fact(",num,")=",str_i,"=",fact)