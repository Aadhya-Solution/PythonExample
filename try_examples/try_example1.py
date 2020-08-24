
try:
	fd=open('/home/shashi/PycharmProjects/pythonExamples/pythonExamples/netData22.txt','r')
except IOError:
    print "Error: cont find the file"
else:
	l=fd.readlines()
	for i in l:
		print i
finally:
	try:
		if not fd.closed:
			fd.close()
		print "Read done"
	except NameError,e1:
		print "I am name erro",e1
		pass