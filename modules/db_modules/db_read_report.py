#!/usr/bin/python
import pymysql

# Open database connection
db = pymysql.connect(db='Employee', user='root', passwd='Test@123', unix_socket="/var/run/mysqld/mysqld.sock")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM EMPLOYEE33 \
       WHERE INCOME >= %d" % (2000)
try:
   # Execute the SQL command
   print("==>",sql)
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()#[[c1,c2,c3],[c1,c2,c3],[c1,c2,c3]]
   print("===",results)
   fd=open('employee_report.txt','w')
   fd.write('='*50+'\n')
   fd.write("Employee Details".center(50)+'\n')
   fd.write('='*50+'\n')
   for row in results:
      #print "==>",row
      fname = row[0]
      lname = row[1]
      age = row[2]
      sex = row[3]
      income = row[4]
      # Now print fetched result
      p="\n%s  %s  %d  %s  %d" % \
             (fname, lname, age, sex, income )
      fd.write(p+"\n")
   fd.write('='*50)
   fd.close()
except:
   print("Error: unable to fecth data")

# disconnect from server
db.close()