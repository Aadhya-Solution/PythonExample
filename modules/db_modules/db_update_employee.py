import MySQLdb
global db
global c
db=MySQLdb.connect(db='Employee', user='root', passwd='Test@123', unix_socket="/var/run/mysqld/mysqld.sock")
c=db.cursor()

def update_details(age,salary):
    sql="update EMPLOYEE33 set age=%d where income>=%d"%(age,salary)
    sql2="update employee2 set income=%d where first_name='%s'"%(5000,"abc")
    print(sql)
    try:
        c.execute(sql)
        db.commit()
    except:
        print("Got error")
        db.rollback()
#clled the defination
update_details(60,3000)
