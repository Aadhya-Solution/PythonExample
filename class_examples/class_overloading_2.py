def f(a,l=[]):
    l.append(a)
    return l
    
    
print f(1)
print f(2)
print f(3)


def fun(a,*b):
    t=a
    for i in b:
        t=t+i
    return t


fun(a,b)
fun(a,b,c)