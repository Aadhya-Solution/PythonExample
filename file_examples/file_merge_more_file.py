def readFile(file):
    f=open(file,'r')
    return f.readlines()
global f2
f2=open('out.txt','a')

def writeFile(l):
	for i in l:
		f2.write(i)

l=['1.txt','2.txt','3.txt']
for eachFile in l:
    l2=readFile(eachFile)
    writeFile(l2)
	
f2.close()