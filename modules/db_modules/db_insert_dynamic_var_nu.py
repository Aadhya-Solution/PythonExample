#!/usr/bin/python
import pymysql
global db
global cursor

db = pymysql.connect(db='Employee', user='root', passwd='Test@123', unix_socket="/var/run/mysqld/mysqld.sock")
# prepare a cursor object using cursor() method
cursor = db.cursor()

def emp_update_details(name,lname,age,sex,income):
	sql = "INSERT INTO EMPLOYEE33(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) \
        VALUES ('{}', '{}', {}, '{}', {} )".format(name.upper(),lname.upper(),age,sex,income)
	try:
		cursor.execute(sql)
		db.commit()
	except Exception as e:
		print("Got error")
		db.rollback()

fd=open('emp.txt','r')
for line in fd.readlines():
	l=line.split()
	emp_update_details(l[0],l[1],int(l[2]),l[3],int(l[4]))
fd.close()
db.close()
