'''Override class __str__ function'''

class MyMeta:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        #"Beautiful class "
        return "str__Name:%s\nAge:%s"%(self.name,self.age)

    def print_std(self):
        print "Name:%s\nAge:%s"%(self.name,self.age)

x = MyMeta("Rama",20)

print x
print "Print the function \n"
x.print_std()