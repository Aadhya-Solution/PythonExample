import os

TEST_GID=501
TEST_UID=527

def show_user_info():
    print 'Effective User  :', os.geteuid()
    print 'Effective Group :', os.getegid()
    print 'Actual User     :', os.getuid(), os.getlogin()
    print 'Actual Group    :', os.getgid()
    print 'Actual Groups   :', os.getgroups()
    return

print 'BEFORE CHANGE:'
show_user_info()
print

try:
    os.setegid(TEST_GID)
except OSError:
    print 'ERROR: Could not change effective group.  Re-run as root.'
else:
    print 'CHANGED GROUP:'
    show_user_info()
    print

try:
    os.seteuid(TEST_UID)
except OSError:
    print 'ERROR: Could not change effective user.  Re-run as root.'
else:
    print 'CHANGE USER:'
    show_user_info()
    print
	
	
'''
$ python os_process_user_example.py

BEFORE CHANGE:
Effective User  : 527
Effective Group : 501
Actual User     : 527 dhellmann
Actual Group    : 501
Actual Groups   : [501, 401, 101, 500, 12, 33, 61, 80, 98, 100, 204, 102]

CHANGED GROUP:
Effective User  : 527
Effective Group : 501
Actual User     : 527 dhellmann
Actual Group    : 501
Actual Groups   : [501, 401, 101, 500, 12, 33, 61, 80, 98, 100, 204, 102]

CHANGE USER:
Effective User  : 527
Effective Group : 501
Actual User     : 527 dhellmann
Actual Group    : 501
Actual Groups   : [501, 401, 101, 500, 12, 33, 61, 80, 98, 100, 204, 102]

'''