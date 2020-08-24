'''__str__ , __repr__ '''

class adder:
     def __init__(self, value=0):
         self.data = value                  # initialize data
     def __add__(self, other):
         self.data += other                 # add other in-place

class addrepr(adder):                      # inherit __init__, __add__
     def __repr__(self):                    # add string representation
         return 'addrepr(%s)' % self.data   # convert to string as code

class addstr(adder):            
     def __str__(self):                     # __str__ but no __repr__
         return '[Value: %s]' % self.data   # convert to nice string

x = addstr(3)
x + 1
print x                                    # runs __str__

print str(x), repr(x)