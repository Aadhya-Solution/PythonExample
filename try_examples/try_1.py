''' jagali
   10 * (1/0)
Traceback (innermost last):
File "<stdin>", line 1
ZeroDivisionError: integer division or modulo
'''
try:
    a=1
    b=0
    div=a/b
    print "Value is :",div
except ZeroDivisionError:
    print "yes"
    pass

'''
try:
    p=10 *(1/0)
    print "Value of p:",p
except:
    p=10*(1/2.0)
    print "Got an exceptrion "
    print "Value is",p
    
 '''   