'''
To convert a relative path to a complete absolute filename, use abspath().

'''


import os.path

for path in [ '.', '..', './one/two/three', '../one/two/three']:
    print '"%s" : "%s"' % (path, os.path.abspath(path))
	

'''
$ python ospath_abspath.py

"." : "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/ospath"
".." : "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW"
"./one/two/three" : "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/ospath/one/two/three"
"../one/two/three" : "/Users/dhellmann/Documents/PyMOTW/src/PyMOTW/one/two/three"
'''