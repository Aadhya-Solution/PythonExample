menu="""
1.ADD
2.SUB
3.MUL
4.DIV
5.EXIT
"""
f=True
while f:
    print menu
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
    p=raw_input("If you want to continue:type Yes or no")
    if p.lower() in ['yes','y']:
        f=True
    else:
        f=False
