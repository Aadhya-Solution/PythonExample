class Report:
    '''
    This is report
    '''
    def __int__(self):
        pass

    def genCustReport(self,name,balance):
        print "-"*30
        print "Name:%s\nBalance:%d" % (name, balance)
        print "-" * 30

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
print "name:",__name__
print "file",__file__
if __name__ == '__main__':
    c=Report()
    name="Shiva"
    bal=20000
    c.genCustReport(name,bal)