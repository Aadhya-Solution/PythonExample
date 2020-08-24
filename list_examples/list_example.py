
n=input("Enter a num:")
l=[]
for i in range(n):
    l.append(i)

print "List Created"
print "L[]:",l

el=input("Enter ele to insert:")
i=input("position")
l.insert(i,el)
print "After Insertion l:"
print ">>",l

print "Pop opertion:",l.pop()
print "remove any elements in l",l
re=input("Enter remove ele:")
print "Removed ele:",re
l.remove(re)
print "After Remove:",l

ex=input("Enter a list:")
l.extend(ex)
print "list ",l





