st="abbaaabbaaccddwwwwrrr"
#[['a',6],['b',4],['c',2]..]
l=[]
for i in st:
    if i.isalpha():
         l.append(i)
l=['a', 'b', 'b', 'a', 'a', 'a', 'b', 'b', 'a', 'a', 'c', 'c', 'd', 'd', 'w', 'w', 'w', 'w', 'r', 'r', 'r']
l=l.sort()
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