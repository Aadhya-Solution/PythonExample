n=input("Nvalue:")
l=[]
for i in range(n):
    ele=raw_input("Enter a String:")
    l.append(ele)

st=""
for e in l:
    st=st+' '+e.upper()

print "OutPut:",st