#!/usr/bin/python
import pymysql
# Open database connection
db = pymysql.connect(db='Employee', user='root', passwd='Test@123', unix_socket="/var/run/mysqld/mysqld.sock")
# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE33 (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT(2),
         SEX CHAR(1),
         INCOME FLOAT )"""
try:
    cursor.execute(sql)
except:
    print("Got Error in mysql execution")
# disconnect from server
db.close()
