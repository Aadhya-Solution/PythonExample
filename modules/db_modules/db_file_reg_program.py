import re
import xlwt
import pymysql
global db
global cursor

db = pymysql.connect(db='Employee', user='root', passwd='Test@123', unix_socket="/var/run/mysqld/mysqld.sock")
# prepare a cursor object using cursor() method
cursor = db.cursor()

def create_table():
    cursor.execute('drop table if exists INTERFACE_TABLE')
    sql = """CREATE TABLE INTERFACE_TABLE (
         INTERFACE  CHAR(20) NOT NULL,
         STATUS  CHAR(20))"""
    cursor.execute(sql)

def config_db(dict_out):
    for intface,status in dict_out.items():
        sql = "INSERT INTO INTERFACE_TABLE(INTERFACE,STATUS) \
        VALUES ('%s', '%s' )" % \
        (intface,status)
        print("..",sql)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

reg=re.compile(r'([\w\-\/\:\.]+)\s*(up|down)\s*(up|down)\s*.*')
def get_interface(fileName):
    out_dict={}
    fd=open(fileName,'r')
    for line in fd.readlines():
        print(line)
        regMatch=reg.search(line)
        if regMatch:
            #if regMatch.group(1).strip().startswith('t1'):
                #out_dict[regMatch.group(1)]=regMatch.group(2)
            out_dict[regMatch.group(1)]=regMatch.group(2)#,regMatch.group(5))
    print(">>>>",out_dict)
    config_db(out_dict)

def xls_report(output):
    wb = xlwt.Workbook()
    sh=wb.add_sheet("Interface Details")
    sh.write(0,0,"Interafce")
    sh.write(0, 1, "Status")
    c=1
    for interface, status in output:
        sh.write(c,0,interface)
        sh.write(c,1,status)
        c=c+1
    wb.save("interface.xls")

def db_fileReport(outPut):
    fd=open("intReport.txt",'w')
    p="-"*50
    fd.write(p)
    fd.write("\n")
    fd.write("Interface deatils".center(50))
    fd.write("\n")
    fd.write(p)
    fd.write('\n')
    for k,v in outPut:
        fd.write("%s    %s"%(k,v))
        fd.write("\n")
    fd.write(p)
    fd.write("\n")
    fd.close()

def db_read():
    sql = "SELECT * FROM INTERFACE_TABLE"
    try:
        cursor.execute(sql)
        outPut=cursor.fetchall()
        xls_report(outPut)
    except:
        print("Error if feaching db")
#print "---->",__name__
def menuz():
    p='''
    1.Get Interface Read Intf detail and update to db
    2.Db to Report
    '''
    while True:
        print(p)
        opt=input("Enter the Opt:")
        print(type(opt))
        if int(opt)==1:
            get_interface("showInterface.txt")
        elif int(opt)==2:
            db_read()
        get_opt=input("Do you want to continue: Type Yes or no")
        if not get_opt.lower() in ['yes','y']:
            break
    db.close()
if __name__ == '__main__':
    create_table()
    menuz()