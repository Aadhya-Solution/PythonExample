#!/usr/bin/python
'''
Suppose you've created a Vector class to represent two-dimensional vectors, 
what happens when you use the plus operator to add them? Most likely Python will yell at you.
'''
class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      print self.a,'===',other.a
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
print "--",v1
v2 = Vector(5,-2)
print "--",v2	
print v1 + v2