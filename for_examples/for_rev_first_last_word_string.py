s=input("Enter A string:")
l=s.split()
for i in range(len(l)):
    if i in [0,len(l)-1]:
        temp=""
        for j in range(len(l[i])-1,-1,-1):
            temp=temp+l[i][j]
        l[i]=temp
print(" ".join(l))

"""
Enter A string:This is my Name Shashi
out put: sihT is my Name ihsahS
"""