print "======File operation=============="
fd=open('abc.txt','w')
c=True
while c==True:
	str1=raw_input("Enter the string to write  ")
	fd.write(str1)
	fd.write('\n')
	c=raw_input("Enter you want to enter the text press Yes")
	if c.lower() in ['yes','y']:
		c=True
	else:
		break

fd.close()
print "Write Done "

print "The out put"
fd=open('abc.txt','r')
for i in fd.readlines():
    print i
fd.close()