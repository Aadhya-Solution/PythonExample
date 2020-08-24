# File: sys-platform-example-1.py
'''
The platform variable contains the name of the host platform:
'''
import sys

# emulate "import os.path" (sort of)...
if sys.platform == "win32":
    import ntpath
    pathmodule = ntpath
elif sys.platform == "mac":
    import macpath
    pathmodule = macpath
else:
    # assume it's a posix platform
    import posixpath
    pathmodule = posixpath

print pathmodule
