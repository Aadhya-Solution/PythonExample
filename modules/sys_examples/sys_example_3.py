'''
The modules dictionary contains all loaded modules. 
The import statement checks this dictionary before 
it actually loads something from disk.
'''

# File: sys-modules-example-1.py
import sys
print sys.modules.keys()

'''
['os.path', 'os', 'exceptions', '__main__', 'ntpath', 'strop', 'nt',
'sys', '__builtin__', 'site', 'signal', 'UserDict', 'string', 'stat']
'''

