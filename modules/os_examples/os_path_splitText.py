'''
splitext() works like split() but divides the path on the extension 
separator, rather than the directory separator.
'''

import os.path

for path in [ 'filename.CVS', 'filename', \
              '/path/to/filename.txt', '/', '' ]:
    print '"%s" :' % path, os.path.splitext(path)

'''
$ python ospath_splitext.py

"filename.txt" : ('filename', '.txt')
"filename" : ('filename', '')
"/path/to/filename.txt" : ('/path/to/filename', '.txt')
"/" : ('/', '')
"" : ('', '')
'''
