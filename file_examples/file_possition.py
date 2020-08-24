print "File opertaion"
fd=open('abc.txt','r+')
print "Current Possition:",fd.tell()
print ">>",fd.read(10)
print "Want to go to 0th possition:",fd.seek(0,0)
print "Current Possition:",fd.tell()
str1="HI its shiva"
fd.write(str1)
fd.write('\n')
fd.seek(0,2)
fd.write("   Rama Rama")
fd.close()
print "Write Done "