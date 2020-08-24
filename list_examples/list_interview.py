l=[1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5] #I/P
l1=[] #[[1,1],[2,2,2],[3,3,3,]]
l2=l[0]
l3=[]
for i in l:
    if i == l2:
        l3.append(i)
    else:
        l1.append(l3)
        l2=i
        l3=[i]
l1.append(l3)
print l1
