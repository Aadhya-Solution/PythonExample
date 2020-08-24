import sys
#python sys_argv_srth.py add 10 20
if len(sys.argv)>1:
    if sys.argv[1]=='add':
        print type(sys.argv[2])
        if type(eval(sys.argv[2])) in [int ,float] \
                and type(eval(sys.argv[3])in [int,float]):
            a,b=eval(sys.argv[2]),eval(sys.argv[3])
            c=a+b
            print "%d+%d=%d"%(a,b,c)
else:
    print "No Argument given \nPlease provide proper Arg"