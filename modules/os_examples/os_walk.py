import os, sys
print "======>",sys.argv
# If we are not given a path to list, use /tmp
if len(sys.argv) == 1:
    root = '/tmp'
else:
    root = sys.argv[1]
print "....>>>",os.walk(root)

for dir_name, sub_dirs, files in os.walk(root):
    print '\n', dir_name
    # Make the subdirectory names stand out with /
    sub_dirs = [ '%s/' % n for n in sub_dirs ]
    # Mix the directory contents together
    contents = sub_dirs + files
    contents.sort()
    # Show the contents
    for c in contents:
        print '\t%s' % c
		

'''
$ python os_walk.py ../zipimport


../zipimport
        __init__.py
        __init__.pyc
        example_package/
        index.rst
        zipimport_example.zip
        zipimport_find_module.py
        zipimport_find_module.pyc
        zipimport_get_code.py
        zipimport_get_code.pyc
        zipimport_get_data.py
        zipimport_get_data.pyc
        zipimport_get_data_nozip.py
        zipimport_get_data_nozip.pyc
        zipimport_get_data_zip.py
        zipimport_get_data_zip.pyc
        zipimport_get_source.py
        zipimport_get_source.pyc
        zipimport_is_package.py
        zipimport_is_package.pyc
        zipimport_load_module.py
        zipimport_load_module.pyc
        zipimport_make_example.py
        zipimport_make_example.pyc

../zipimport/example_package
        README.txt
        __init__.py
        __init__.pyc
'''
