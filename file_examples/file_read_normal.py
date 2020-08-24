fo=open("anilTest.py",'r')

line=fo.read(19) #read chr

print "Line ",line
print "Current position",fo.tell()
print "read line:",fo.readlines()
print "Need To move the begining:",fo.seek(0,0) #gghjgkjk
print "Current position",fo.tell()
for l in fo.readlines(): #['l1','l2','l3']
    print l
fo.close()