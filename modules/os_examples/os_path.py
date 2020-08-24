'''
split() breaks the path into 2 separate parts and returns the tuple. The second element is the 
last component of the path, and the first element is everything that comes before it.
'''

import os.path

for path in [ '/one/two/three', 
              '/one/two/three/',
              '/',
              '.',
              '']:
    print '"%s" : "%s"' % (path, os.path.split(path))
	
	
'''
$ python ospath_split.py

"/one/two/three" : "('/one/two', 'three')"
"/one/two/three/" : "('/one/two/three', '')"
"/" : "('/', '')"
"." : "('', '.')"
"" : "('', '')"
'''