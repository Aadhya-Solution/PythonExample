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
	fd=open('std_report3.txt','w')
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
l=[["Raghu","Ramakrish",34,'M',3000.0],
   ["Raghu","Ramakrish",34,'M',3000.0],
   ["Raghu","Ramakrish",34,'M',3000.0],
   ["Raghu","Ramakrish",34,'M',3000.0],
   ["Raghu","Ramakrish",34,'M',3000.0]]
std_report2(l)