

import os
import stat
path=os.path.join(os.getcwd(),"abc.txt")

print "==>",os.access(path,os.R_OK)

print "Write Mode only:",os.chmod(path,stat.S_IWRITE)


print "==>",os.access(path,os.R_OK)
print "==>",os.access(path,os.W_OK)

print "Write Mode only:",os.chmod(path,stat.S_IWRITE)
print "==>",os.access(path,os.W_OK)
print "file exist:",os.access(path,os.F_OK)


print "getcwdu:",os.getcwdu(),os.getcwd()