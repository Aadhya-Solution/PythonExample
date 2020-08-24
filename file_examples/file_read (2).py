
fo=open('inPut2.txt','r')

for line in fo.readlines():
    print line

for i in range(6):
    line= fo.next()
    print "line is ",i,":",line
    
fo.close()