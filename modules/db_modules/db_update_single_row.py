import pymysql

db=pymysql.connect(db="Employee", user='root', passwd='Test@123', unix_socket="/var/run/mysqld/mysqld.sock")

c= db.cursor()

sql = """INSERT INTO EMPLOYEE33(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('Sita', 'Rama', 20, 'F', 2000)
       """
c.execute(sql)
db.commit()
db.close()
