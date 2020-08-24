fd=open('std.txt','r+')
print "Name of File:",fd.name
str1="This is the 10th Line\n"
fd.seek(0,2)
print "possition:",fd.tell()
fd.write(str1)
fd.seek(0,0)
print "possition:",fd.tell()
for line in fd.readlines():
    print line
fd.seek(0,0)
print "After print ssition:",fd.tell()
#----------------
fd=open('std.txt','r+')
try:
    for i in range(1,100,2):
    	line = fd.next()
        print "%d --> %s"%(i,line.upper())
except:
    print "Yes its passed"
    pass

fd.close()