'''
Class Inheritance:

Instead of starting from scratch, you can create a class by deriving it from
 a preexisting class by listing the parent class in parentheses after the new class name.

The child class inherits the attributes of its parent class, and you can use those attributes 
as if they were defined in the child class. A child class can also override data members and methods from the parent.

'''

#!/usr/bin/python
class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"
   def parentMethod(self):
      print 'Calling parent method'
   def setAttr(self, attr):
      Parent.parentAttr = attr
   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class B: # define child class
   def __init__(self):
      print "Calling B constructor"
   def parentMethod(self):
      print 'Calling B method'

class Child(Parent,B): # define child class
   def __init__(self):
      print "Calling child constructor"
   def childMethod(self):
      print 'Calling child method'

c = Child()          # instance of child
print dir(c)
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method