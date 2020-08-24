try:
    os.getcwd
    str1=1+"Shiva"    
except(TypeError):
    str1=str(1)+"Shiva"
    print "==>",str1
except(NameError):
    import os
    print "Path is:",os.getcwd()
