class Student:
    def __init__(self,name,age):
        self.name=name
        self.age= age
    def print_std(self):
        print "Name:",self.name
        print "Age",self.age

if __name__ == '__main__':
    p=Student('Shiva',20)
    p1=Student('Rama',21)

    p.print_std()
    p1.print_std()