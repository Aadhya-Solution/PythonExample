'''
The two functions strptime() and strftime() convert 
between struct_time and string representations of time values. 
There is a long list of formatting instructions available to support
 input and output in different styles.
'''

import time
now = time.ctime()
print now
parsed = time.strptime(now)
print ">>",parsed
print "---",time.strftime\
    ("%a %b %d %H:%M:%S %Y", parsed)

'''
$ python time_strptime.py
Sun Mar  9 13:01:19 2008
(2008, 3, 9, 13, 1, 19, 6, 69, -1)
Sun Mar 09 13:01:19 2008
'''
