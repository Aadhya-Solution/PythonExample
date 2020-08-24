import os

print 'Testing:', __file__
print 'Exists:', os.access(__file__, os.F_OK)
print 'Readable:', os.access(__file__, os.R_OK)
print 'Writable:', os.access(__file__, os.W_OK)
print 'Executable:', os.access(__file__, os.X_OK)

'''
Filesystem Permissions:
The function access() can be used to test the access rights a process has for a file.

$ python os_access.py

Testing: os_access.py
Exists: True
Readable: True
Writable: True
Executable: False
'''