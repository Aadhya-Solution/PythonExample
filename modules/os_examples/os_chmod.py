#!/usr/bin/python

import os, stat

# Assuming /tmp/foo.txt exists,
# Set a file execute by the group.
os.chmod("abc.txt", stat.S_IXGRP)
# Set a file write by others.
os.chmod("abc.txt", stat.S_IWUSR)
print "Changed mode successfully!!"

'''
os.chmod(path, mode);

Parameters

    path -- This is the path for which mode would be set.

    mode -- This may take one of the above mentioned values or bitwise ORed combinations of them.

The method chmod() changes the mode of path to the passed numeric mode. The mode may take one of the following values or bitwise ORed combinations of them:

    stat.S_ISUID: Set user ID on execution.

    stat.S_ISGID: Set group ID on execution.

    stat.S_ENFMT: Record locking enforced.

    stat.S_ISVTX: Save text image after execution.

    stat.S_IREAD: Read by owner.

    stat.S_IWRITE: Write by owner.

    stat.S_IEXEC: Execute by owner.

    stat.S_IRWXU: Read, write, and execute by owner.

    stat.S_IRUSR: Read by owner.

    stat.S_IWUSR: Write by owner.

    stat.S_IXUSR: Execute by owner.

    stat.S_IRWXG: Read, write, and execute by group.

    stat.S_IRGRP: Read by group.

    stat.S_IWGRP: Write by group.

    stat.S_IXGRP: Execute by group.

    stat.S_IRWXO: Read, write, and execute by others.

    stat.S_IROTH: Read by others.

    stat.S_IWOTH: Write by others.

    stat.S_IXOTH: Execute by others.
'''
