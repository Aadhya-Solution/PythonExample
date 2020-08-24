class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"
   def Method(self):
      print 'Calling parent method'
class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"

   def Method(self):
      print 'Calling child method'

p=Parent()
print dir(p)
print p.Method()
print "====child===="
c=Child()
print dir(c)
c.Method()