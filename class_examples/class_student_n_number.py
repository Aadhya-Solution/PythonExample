class Student:
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def print_std(self):
        print "Name:",self.name
        print "Age",self.age

if __name__ == '__main__':
    l=[]
    f=True
    while f:
        name=raw_input("Enter Name:")
        age=input("Enter Age:")
        p=Student(name,age)
        l.append(p)
        opt=raw_input("If u want to cont press Y:")
        if opt in ['Y','y']:
            f=True
        else:
            f=False
    ele=raw_input("Want to display? Press Y")
    if ele in ['Y','y']:
        print "+"*50
        print "Std Report".center(50)
        print "+"*50
        for e in l:
            print "%s       %d"%(e.name,e.age)
    else:
        print "Bye"