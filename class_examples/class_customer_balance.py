
class db:
    def __init__(self):
        pass
    def connect(self):
        pass

    def create(self):
        pass

    def connection_close(self):
        pass

    def update(self,data):
        pass

class Report:
    def __init__(self):
        pass
    def print_ack(self,details):
        print "-"*20
        print "  Ack  "
        print "-"*20
        for k,v in details.items():
            print k,":",v
        print "-"*20

class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:
    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """
    def __init__(self, name='', balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance
        self.pin=""
        self.dob=''
        self.loc=''
        self.address=''
        self.tracDict={}
        self.trac_id=1
    def updateDetails(self):
        self.dob=raw_input("Enter DOB(dd/mm/yyyy):")
        self.loc=raw_input("Enter Location:")
        self.address=raw_input("Enter the address:")
        print "Update Done"
    def display_details(self):
        p="="*50
        print p
        print "Name:%s\nDOB:%s\nLoc:%s\n"%(self.name,self.dob,self.loc)
        print p
    def setPin(self):
        newPin=raw_input("Enter a new Pin:")
        self.pin=newPin
    def getPin(self):
        print "Pin is %s"%(self.pin)
    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        while True:
            getPin=raw_input("Enter pin to withdraw:")
            if getPin == self.pin:
                if amount > self.balance:
                    print 'Amount greater than available balance.'
                    amount = input("Enter Amount:")
                else:
                    self.balance -= amount
                    break
            else:
                print "Wrong Pin entered"
        self.tracDict[self.trac_id]={"wd":{'bal':self.balance,'amt':amount}}
        self.trac_id=self.trac_id+1
        return self.balance
    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        self.tracDict[self.trac_id] = {"dp": {'bal': self.balance, 'amt': amount}}
        self.trac_id = self.trac_id + 1
        return self.balance
    def pinchange(self):
        newPin=raw_input("Eneter new pin:")
        self.pin=newPin
    def check_balance(self):
        print "Balance Amount:",self.balance

    def print_ack(self):
        p=Report()
        p.print_ack({"Name":self.name,
                     "Bal":self.balance})

    def displayTrasaction(self):
        for id,eachTras in self.tracDict.items():
            print id,"==>",eachTras
def menu():
    p='''
    1.Create Customer
    2.SetPin
    3.Update Detailds
    4.WithDraw
    5.Deposit
    6.Pinchange
    7.search Customer
    8.get Ack
    9.Check Balance
    10.Trasaction Details
    11.Exit
    '''
    print p
f=True
l=[]
while True:
    menu()
    Opt=input("Enter the Option:")
    if Opt==1:
        name=raw_input("Enter Name:")
        c=Customer()
        c.name=name
        l.append(c)
        c.print_ack()
    elif Opt==2:
        c.setPin()
    elif Opt==3:
        c.updateDetails()
    elif Opt==4:
        amt=input("Withdraw amount :")
        c.withdraw(amt)
    elif Opt==5:
        amt=input("Deposit amount:")
        c.deposit(amt)
    elif Opt==9:
        c.check_balance()
    elif Opt == 10:
        c.displayTrasaction()
    else:
        print "Wrong Option"
    ex=raw_input("Do you want to continue: press Yes or no:")
    if not ex.upper() in ['YES',"Y"]:
        break