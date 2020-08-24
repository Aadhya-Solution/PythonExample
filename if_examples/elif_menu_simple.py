line="+"+"="*50+'+'
title='+'.ljust(10)+"Arthemetic Opertaion"+'+'.rjust(22)
menu="""
|1.ADD
|2.SUB
|3.MUL
|4.DIV
|5.EXIT
"""
print line
print title
print line
print menu
print line
getInput=input("Enter the option:")
if getInput==1:
    print "Add numbers"
elif getInput==2:
    print "SUB num"
elif getInput==3:
    print "MUL num"
elif getInput==4:
    print "DIV num"
elif getInput==5:
    print "EXIT Bye"
print line