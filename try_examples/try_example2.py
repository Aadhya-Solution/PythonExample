l=[1,2,3,4,5]
#sum1=0
for i in l:
	try:
		print "==>"
		sum1=sum1+i
		print "===",sum1
	except (IOError,NameError,TypeError,ZeroDivisionError):
		print "Yes erro is comming"
		break
	'''
	finally:
		print "I am in finaly"
		print ">>",i
#print "Sum:",sum1
'''
	