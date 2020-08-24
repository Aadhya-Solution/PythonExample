print "File opertaion"
fd=open('abc.txt','a')
print "Current Possition:",fd.tell()
fd.write('\n')
c=True
while c==True:
	str1=raw_input("Enter the string to write")
	fd.write(str1)
	fd.write('\n')
	c=raw_input("Enter you want to enter the text press Yes")
	if c.lower() in ["yes",'y']: # c.upper in ["YES","Y"]
		c=True
	else:
		break

fd.close()
print "Write Done "