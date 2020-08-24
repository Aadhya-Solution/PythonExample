'''
File Read operation
'''

fd=open('abc.txt','r')
print fd.read(7)
for line in fd.readlines():
    print line

fd.close()






'''
print "Next"
print fd.tell()
print "After Tell"
print fd.readlines()
'''