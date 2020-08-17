class Customer:
    def __init__(self,name="",bal=0):
        self.name = name
        self.bal = bal
        self.loc = ""
        self.city = ""
        self.cust_id = ""
    def create_customer(self):
        cust_name = input("Eneter Name:")
        cust_id = input("Enter Cust Id:")
        self.cust_id = cust_id
        self.name = cust_name

    def update_customer(self):
        self.loc = input("Loc:")
        self.city = input("City:")
        self.contact = input("Contact:")

    def deposit(self):
        amt = input("Eneter the amount :")
        self.bal = self.bal + amt

    def withdraw(self):
        amt = input("Enet amount to withdraw:")
        pin = input("Eneter the PIN:")
        if self.pin == pin:
            if amt < self.bal:
                self.bal = self.bal - amt
            else:
                print("Amount should be less then the balanc")

    def set_pin(self):
        pin= input("Eneter pin :")
        self.pin = pin

    def balance_display(self):
        print("Balance:",self.bal)

    def display_cust_details(self):
        print("Name:%s\nContact:%s\nLOc:%s\nCity:%s"%(self.name,self.contact,self.loc,self.city))

def customer_options():
    menu="""
    1. Cust Create
    2. Set PIN
    3. Update customer details 
    4. deposit
    5. withdraw
    6. Pin change 
    7. Check balance
    8. exit
    """
    print(menu)

while True:
    customer_options()
    opt = input("Eneter the Option:")
    if opt ==1:
        cust = Customer()
        cust.create_customer()
    elif opt ==2:
        cust.set_pin()
    elif opt == 3:
        cust.update_customer()
    elif opt== 4:
        cust.deposit()
    elif opt == 5:
        cust.withdraw()
    elif opt == 7:
        cust.balance_display()
    elif opt == 8:
        cust.display_cust_details()
    elif opt ==9:
        print("Bye")
        break



