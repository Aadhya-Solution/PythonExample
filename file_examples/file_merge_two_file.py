def readFile(file):
    f=open(file,'r')
    return f.readlines()

def writeFile(l,l1):
    f2=open('out.txt','w')
	for i in l:
		f2.write(i)
	for i1 in l2:
		f2.write(i1)
    f2.close()		
l=readFile('1.txt')
l2=readFile('2.txt')
writeFile(l,l2)

 
   f2.close()