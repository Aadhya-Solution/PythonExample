import os
path='aaa.txt'
fd=os.open(path,os.O_APPEND|os.O_RDWR)
os.write(fd,"ShivaShashi")#fd.write()
os.close(fd)

# To read the file
print "Reading here"
fd=os.open(path,os.O_RDONLY)
print os.read(fd,10)#fd.read(10)
os.close(fd)#fd.close()



#dst='E:\pythonExamles\hello.py'
#os.link(path,dst)
