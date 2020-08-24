fo=open('inPut2.txt','r')

try:
    for i in range(100):
        l= fo.next()
        print "line is ",i,":",l.upper()
except :
    pass
fo.close()