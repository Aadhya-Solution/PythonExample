try:
    fd=open("test1.txt",'r')
    for i in range(8):
        print(fd.__next__())
except StopIteration:
    pass
fd.close()

# fd.seek(0,0)
#        0-->starting 0th poss
# fd.seek(ch,1)
#        1--- Current postion
#     +n --- FWD   -n ---> Rev move
#     fd.seek(-2,1)
#                 ---------
#                 ---(-2 back)
#                 ------(3)...|
#
# fd.seek(ch,2)
#        2----> end
# write , writelines, read , readline, readlines-->list
# name, mode, closed
# closed --> True
#    False
#     fd.close()
# next
# w+,r+,a+
# w+ --> write and read

