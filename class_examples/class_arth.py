class Operation:
    def __init__(self,n1,n2):
       self.a=n1
       self.b=n2

    def add(self):
        self.sum=self.a+self.b
        print "%d+%d=%d"%(self.a,self.b,self.sum)
    def sub(self):
        self.sub=self.a-self.b
        print "%d-%d=%d"%(self.a,self.b,self.sub)

    def pow(self):
        self.p=self.a**self.b
        print "%d^%d=%d"%(self.a,self.b,self.p)

c=Operation(2,3)
print  c.a,c.b
c.add()
c.sub()
