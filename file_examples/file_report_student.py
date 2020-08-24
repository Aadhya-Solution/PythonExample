global std_list

def std_report(std_name1):
	st="="*20
	fd=open('std_report2.txt','w')
	for std in std_list:
		if std_name1 in std['Name']:
			fd.write("     Student Details     \n")
			fd.write(st+'\n')
			fd.write("Name:%s\nDOB:%s\nFathe Name:%s\nAddress:%s\nClass:%s\nContact:%s\nTotal:%d\nResult:%s\n"%(std['Name'],std['DOB'],std['Father'],std['Address'],std['Class'],std['Mobile'],std['Total'],std['Result']))
			fd.write(st+'\n')
			fd.close()
			break
	else:
		print "Student Not Found"

std_list=[]
d={'Name':"Shiva",'DOB':'10/02/1990','Father':"ABC",'Address':'BTM','Class':98,'Mobile':98799,'Total':99,'Result':"Pass"}
std_list.append(d)
std_report("Shiva")