
fd=open('abc.txt','r')
print fd.read(10)
for line in fd.readlines():
    print line
fd.close()








'''
#\nHow r you

fd.write('\n')
fd.write("Yes i am here")

open(filename,mode)
open('/home/shahsi/documets/test.txt',)
mode --w ---> w,w+,bw,bw+
    r  --> r,r+,br,br+
    a  --> a,a+,ba,ba+
'''