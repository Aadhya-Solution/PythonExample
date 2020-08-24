try:
   a=input("Enter Value:")
   b=input("Enter Value:")
   c=a/b
   print "c:",c
except (ZeroDivisionError,TypeError):
   print "I got error"