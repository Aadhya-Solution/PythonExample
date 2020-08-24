def std_report(std_name1):
	st="="*20
	fd=open('std_report.txt','w')
	for std in std_list:
		if std_name1 in std['Name']:
			fd.write("     Student Details     \n")
			fd.write(st+'\n')
			fd.write("Name:%s\nDOB:%s\nFathe Name:%s\nAddress:%s\nClass:%s\nContact:%sTotal:%d\nResult:%s\n"%(std['Name'],std['DOB'],std['Father'],std['Address'],std['Class'],std['Mobile'],std['Total'],std['Result']))
			fd.write(st)
			fd.write(st+'\n')
			fd.close()
			break
	else:
		print "Student Not Found"

def std_complete_report():
	st="="*20
	fd=open('std_complete_report.txt','w')
	fd.write(st+'\n')	
	fd.write("     Student Details     \n")
	fd.write(st+'\n')
	fd.write("|Name|DOB|Fathe Name|Address|Class|Contact|Total|Result|\n")
	fd.write(st+'\n')
	for std in std_list:
			fd.write("%s:%s:%s:%s:%s:%s:%d%s\n"%(std['Name'],std['DOB'],std['Father'],std['Address'],std['Class'],std['Mobile'],std['Total'],std['Result']))
			fd.write('\n')
			
	fd.write(st+'\n')
	fd.close()

global std_list
std_list=[]
import random

def std_registration():
	check_std=True
	while check_std:
		std_name = raw_input("Enter Student Name:")
		std_date = raw_input("Enter Student DOB dd/mm/yyyy:")
		std_father_name= raw_input("Enter Student Father NAme:")
		std_address= raw_input("Enter Student Address:")
		std_contact = raw_input("Enter Student ContactNumber:")
		std_class = raw_input("Enter Student Class:")
		std_reg=random.randint(10,100)
		std_list.append({"RegistratioNo":std_reg,"Name":std_name,"DOB":std_date,"Address":std_address,"Class":std_class,"Mobile":std_contact,"Father":std_father_name})
		c=raw_input("You want Add One more Student, Type Y opr Yes")
		if c.lower() in ['y','yes']:
			check_std=True
		else:
			break
def std_marks_update():
	check_marks=True
	while check_marks:
		c_name=raw_input("If you want to Enter Name or not")
		if c_name in ['y','yes','Y',"Yes"]:
			std_reg= raw_input("Enter the Stduent Name:")
			for i in std_list:
				if std_reg is i['Name']:
					print "Student Found. Please enter the Subjects marks:"
					std_maths,std_sc,std_ss=input("Enter Maths,SC,SS by comma :")
					i.update({'Maths':std_maths,"Social Scince":std_sc,"Social Sc":std_ss})
					total=i['Maths']+i['Social Scince']+i['Social Sc']
					if total<150:
						result='FAIL'
					else:
						result='PASS'
					i.update({"Total":total,"Result":result})
			else:
				print "Entered Reg Number is Wrong"
		else:
			print "If You want the enter for All student,type ALL:"
			c_all=raw_input("Type ALL:")
			if c_all=="ALL":
				for i in std_list:
					print "Student Found. Please enter the Subjects marks:"
					std_maths,std_sc,std_ss=input("Enter Maths,SC,SS by comma :")
					i.update({'Maths':std_maths,"Social Scince":std_sc,"Social Sc":std_ss})
					total=i['Maths']+i['Social Scince']+i['Social Sc']
					if total<150:
						result="FAIL"
					else:
						result="PASS"
					i.update({"Total":total,"Result":result})
			else:
				break

def main_prg():
	c=True	
	while c==True:
		str_opt="""
		1.Add Student Details
		2.Add Student Marks and sem details
		3.Sudent Report
		4.Complete Sutunedts report
		5.If you want to contine
		6.Quit
		"""
		print str_opt
		opt=input("Enter the opt")
		if opt==1:
			std_registration()
		elif opt==2:
			std_marks_update()
		elif opt==3:
			std_name1=raw_input("Enter the Student Name:")
			std_report(std_name1)
		elif opt==4:
			std_complete_report()
		elif opt==5:
			c=True
		elif opt==6:
			print "Good bye ..."
			break

main_prg()