import re
pat=re.compile(r'(Cisco[\-\_\:\d\w]+)')
pat1=re.compile(r'([\w\.\-\_\:\d\/]+)\s*(up|doon)\s*(up|down)\s*(\w*)\s*.*')
fd=open('showInterface.txt','r')
for i in fd.readlines():
    m=pat1.search(i)
    if m:
        print m.group(1),m.group(2)

fd.close()
