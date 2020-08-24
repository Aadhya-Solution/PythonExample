def std_report2(results):
	'''
+------------+-----------+------+------+--------+
| FIRST_NAME | LAST_NAME | AGE  | SEX  | INCOME |
+------------+-----------+------+------+--------+
| Raghu      | Ramakrish |   34 | M    |   3000 |
| Sita       | Ramakrish |   34 | F    |   3000 |
| Raghu      | Prasadh   |   34 | M    |   6000 |
| abc        | Ramakrish |   34 | M    |   3000 |
| xyz        | Ramakrish |   34 | F    |   3000 |
| Raghu      | Prasadh   |   34 | M    |   6000 |
+------------+-----------+------+------+--------+
'''
	p='-'
	line_print='+ %10s + %10s + %4s + %3s + %6s +'%('-'*10,'-'*10,'-'*4,'-'*3,'-'*6)
	fd=open('std_report2.txt','w')
	tatle_str="| FIRST_NAME | LAST_NAME | AGE  | SEX  | INCOME |"
	fd.write(line_print+'\n')
	fd.write(tatle_str+'\n')
	fd.write(line_print+'\n')
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		eachrow="| %10s | %10s | %4s | %3s | %6s |"%(fname,lname,age,sex,income)
		fd.write(eachrow+'\n')
	fd.write(line_print)
	fd.close()

def get_from_db():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","moon01","studentdb" )
	cursor = db.cursor()
	sql = "SELECT * FROM EMPLOYEE WHERE INCOME >= %d" % (2000)

	try:
		cursor.execute(sql)
		results = cursor.fetchall()#[[c1,c2,c3],[c1,c2,c3],[c1,c2,c3]]
		std_report2(results)
	except:
		print("Error: unable to fecth data")
	db.close()

def std_report(name,*marks,**details):
	st="="*20 # ======================
	fd=open('aaa.txt','w')
	total=0
	for i in marks:
		total+=i
	fd.write(st+'\n')
	fd.write("     Student Details     \n")
	fd.write(st+'\n')
	fd.write("Name:%s\n"%name)
	for k,v in details.items():
		fd.write("%s :  %s\n"%(k,str(v)))
	fd.write("Total:%s\n"%total)
	fd.write(st)
	fd.close()

std_report('SHiva',45,56,67,age=20,add="BTM",contact=999888)
get_from_db()
'''
while c==True:
	str_opt="""
	1.Add Student Details
	2.Add Student Marks and sem details
	3.Sudent Report
	4.Complete Sutunedts report
	5.Delete a record
	""""
	print str_opt
	opt=input("Enter tthe opt")
	if opt==1:
		std_add_fun()
	elif opt==2:
		std_marks_fun()
	elif opt==3:
		std_report()

Regular expression 
os,random,math,time,cal,sys
'''