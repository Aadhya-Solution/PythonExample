
try:
    f = open('test5.txt','r')
    s = f.readlines()
    try:
        a=10
    except:
        print("Smoe things ")
except (IOError):
    print("Opps Got Exception")
else:
    for i in s:
        print(i)
finally:
    try:
        f.close()
    except NameError:
        print("Opps its not defined")
    print("I am closing file")