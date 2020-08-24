l=[1,1,2,2,2,3,3,3,4,4,4]
#[[2,1],[3,2],[4,3],[4,4]]
#-->[[2,1], [3,2], [3,3], [4,4]]
l1=[] #[[1,1],[2,2,2],[3,3,3,]]
l2=l[0]
l3=[]
wc=0
temp=[0]
for i in l:
    if i == l2:
        wc=wc+1
        temp=i
    else:
        l3=[wc,temp]
        l1.append(l3)
        l2=i
        wc=1
l1.append([wc,temp])
print l1