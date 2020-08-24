'''
Paths assembled from separate strings using join() or with embedded variables might 
end up with extra separators or relative path components. Use normpath() to clean them up:
'''
import os.path
for path in [ 'one//two//three', 
              'one/./two/./three', 
              'one/../one/two/three',
              ]:
    print path, ':', os.path.normpath(path)
'''
$ python ospath_normpath.py

one//two//three : one/two/three
one/./two/./three : one/two/three
one/../one/two/three : one/two/three
'''