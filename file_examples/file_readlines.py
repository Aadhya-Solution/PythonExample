'''
File Readlines operation
'''
fd=open('123.txt','r')
for line in fd.readlines():
	print "line:",line.upper()
fd.close()
