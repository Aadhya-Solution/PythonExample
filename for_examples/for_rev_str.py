st=raw_input("Enter the String:")
reSt=''
for i in range(len(st)-1,-1,-1):
    reSt=reSt+st[i]
print("Original String:",st)
print("Reversed String",reSt)
print('='*30)
st=input("Type one line:")
stList=st.split()#['Shiva','is','coming','to','Blore']
stLine=''
for eachWord in stList:
    temp=''
    for i in range(len(eachWord)-1,-1,-1):
        temp=temp+eachWord[i]
    print("-->",stLine)
    stLine=stLine+' '+temp

print("Reverse word Line:",stLine)