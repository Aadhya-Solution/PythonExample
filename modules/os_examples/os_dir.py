import os

dir_name = 'os_directories_example'

print 'Creating', dir_name
os.makedirs(dir_name)
file_name = os.path.join(dir_name, 'example.txt')
print 'Creating', file_name
f = open(file_name, 'w')
try:
    f.write('example file')
finally:
    f.close()

print 'Listing', dir_name
print os.listdir(dir_name)

print 'Cleaning up'
os.unlink(file_name)
os.rmdir(dir_name)

'''
$ python os_directories.py

Creating os_directories_example
Creating os_directories_example/example.txt
Listing os_directories_example
['example.txt']
Cleaning up
'''