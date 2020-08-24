'''
File Read operation
'''
fd=open('abc.txt','r+')
print "==>",fd.tell()
print fd.read(20)
print "Current possition:",fd.tell()
fd.seek(0,0)
print "After seek(0,0) possition:",fd.tell()
print fd.read(30)
print "Current possition:",fd.tell()
fd.seek(0,1)
print "After seek(0,1) possition:",fd.tell()
print fd.read(30)
print "After seek(0,1) possition:",fd.tell()
fd.seek(0,2)
print "After seek(0,2) possition:",fd.tell()
fd.write("Radha")
fd.close()
