fo=open('inPut2.txt','w')
print "File Name:",fo.name
print "File Mode:",fo.mode

fo.write("Python is language\n")
fo.write("Its is great.....\n")
fo.write("Rama is great.....\n Shita is also\n")

if fo.closed :
    print "File is closed"
else:
    print "File is not closed"
    fo.close()