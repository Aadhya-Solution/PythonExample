line="+"+"="*50+'+'
title='+'.ljust(10)+"Arthemetic Opertaion".center(20)+'+'.rjust(22)
menu="""
|1.ADD
|2.SUB
|3.MUL
|4.DIV
|5.EXIT
"""
flag=True
while flag:
    print(line)
    print(title)
    print(line)
    print(menu)
    print(line)
    getInput=int(input("Enter the option:"))
    if getInput==1:
        a=int(input('Enter Num1:'))
        b=int(input('Enter Num2:'))
        c=a+b
        print("%s+%s=%s"%(a,b,c))
        print("Add numbers")
    elif getInput==2:
        print("SUB num")
    elif getInput==3:
        print("MUL num")
    elif getInput==4:
        print("DIV num")
    elif getInput==5:
        print("EXIT Bye")
    print(line)
    get_opt=input("Enetr yes if you want to continue:")
    if get_opt.lower() in ['yes','y']:
        flag=True
    else:
        flag=False