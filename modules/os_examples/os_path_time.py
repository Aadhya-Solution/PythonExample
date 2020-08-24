'''
Besides working with paths,
os.path also includes some functions
for retrieving file properties,
which can be more convenient than calling
os.stat():
'''

import os.path
import time
#abs
print 'File       :', __file__
print 'Access time  :', time.ctime(os.path.getatime(__file__))
print 'Modified time:', time.ctime(os.path.getmtime(__file__))
print 'Change time  :', time.ctime(os.path.getctime(__file__))
print 'Size         :', os.path.getsize(__file__)

'''
aaa
$ python ospath_properties.py

File         : ospath_properties.py
Access time  : Thu Feb 21 06:36:29 2013
Modified time: Sat Feb 19 19:18:23 2011
Change time  : Sat Jul 16 12:28:42 2011
Size         : 495
'''