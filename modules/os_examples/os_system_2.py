import os
import time

print 'Calling...'
os.system('date')

print 'Sleeping...'
time.sleep(5)

'''
$ python -u os_system_background.py

Calling...
Thu Feb 21 06:36:14 EST 2013
Sleeping...
Thu Feb 21 06:36:18 EST 2013
'''