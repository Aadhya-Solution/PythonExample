class TextReport:
    '''
    This is report
    '''
    def __init__(self):
        self.fd=open("cust_report.txt",'w')

    def genCustReport(self,name,balance):
        self.fd.write("-"*30+'\n')
        self.fd.write("Name:%s\nBalance:%d" % (name, balance))
        self.fd.write("-" * 30)

    def file_close(self):
        self.fd.close()

    def genTransReport(self):
        pass

    def getCustDetails(self,cust):
        print "-"*30
        print cust.name
        print cust.balance
        print cust.pin
        print cust.dob
        print cust.loc
        print "-"*30
