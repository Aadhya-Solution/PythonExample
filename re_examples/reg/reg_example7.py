'''
finditer() returns an iterator that produces Match instances instead of the strings returned by findall().
'''

import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found "%s" at %d:%d' % (text[s:e], s, e)
	
	
	
'''
Output:
$ python re_finditer.py

Found "ab" at 0:2
Found "ab" at 5:7
'''
