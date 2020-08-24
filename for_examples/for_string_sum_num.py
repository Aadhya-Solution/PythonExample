st=input("Enter Num:")
l=st.split()
s=0
l1=[]
for i in l:
    if i.isdigit():
        s=s+eval(i)
        l1.append(i)
print(" +".join(l1),"=",s)