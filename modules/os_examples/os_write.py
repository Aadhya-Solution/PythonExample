# !/usr/bin/python

import os, sys
# Open file
fd = os.open("f1.txt",os.O_RDWR|os.O_CREAT)
# Writing text
ret = os.write(fd,"This is test this is ahs")

# ret consists of number of bytes written to f1.txt
print "The number of bytes written: "
print  ret

print "written successfully"

# Close opened file
os.close(fd)
print "Closed the file successfully!!"

'''
os.write(fd, str)
Parameters

    fd -- This is the file descriptor.

    str -- This is the string to be written.
the number of bytes written:
12
written successfully 
Closed the file successfully!!
'''
