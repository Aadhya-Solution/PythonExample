# File: sys-modules-example-1.py
'''
The modules dictionary contains all
loaded modules.
The import statement checks this
dictionary before it actually loads
something from disk.

As you can see from the following example, 
Python loads quite a bunch of modules
before it hands control over to your script.
'''
import sys
print sys.modules
for k,v in sys.modules.items():
    print k,"-->",v

## ['os.path', 'os', 'exceptions', '__main__', 'ntpath', 'strop', 'nt',
## 'sys', '__builtin__', 'site', 'signal', 'UserDict', 'string', 'stat']
