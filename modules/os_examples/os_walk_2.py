# !/usr/bin/python

import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
        
        

'''
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])

Parameters

    top -- Each directory rooted at directory, yields 3-tuples, i.e., (dirpath, dirnames, filenames)

    topdown -- If optional argument topdown is True or not specified, directories are scanned from top-down. If topdown is set to False, directories are scanned from bottom-up.

    onerror -- This can show error to continue with the walk, or raise the exception to abort the walk.

    followlinks -- This visits directories pointed to by symlinks, if set to true.

./tmp/test.py
./.bash_logout
./amrood.tar.gz
./.emacs
./httpd.conf
./www.tar.gz
./mysql.tar.gz
./test.py
./.bashrc
./.bash_history
./.bash_profile
./tmp


'''