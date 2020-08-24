a = [1,2,3,4]
b = [17,12,11,10]

c = [-1,-4,5,9]
f= lambda x,y:x+y
p=map(f, a,b)
#[18, 14, 14, 14]
print "Sum of two list:",p
p1=map(lambda x,y,z:x+y+z, a,b,c)
#[17, 10, 19, 23]
print "adding three list element:",p1
p2=map(lambda x,y,z:x+y-z, a,b,c)
#[19, 18, 9, 5]
print "x+y-z of all the element :",p2