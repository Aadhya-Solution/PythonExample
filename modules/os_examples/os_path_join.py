
'''
Besides taking existing paths apart, you will frequently need to build paths from other strings.

To combine several path components into a single value, use join():
'''

import os.path

for parts in [ ('one', 'two', 'three'),
               ('/', 'one', 'two', 'three'),
               ('/one', 'two'),
               ]:
    print ">>",type(parts)
    print parts, ':', os.path.join(*parts)
	
'''
$ python ospath_join.py

('one', 'two', 'three') : one/two/three
('/', 'one', 'two', 'three') : /one/two/three
('/one', '/two', '/three') : /three


'''
