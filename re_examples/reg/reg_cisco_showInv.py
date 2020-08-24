import re
reg=re.compile('^\s*PID\s*:\s*([\w\-\/]+)\s*.*SN:\s*(\w+)')
def get_pid(fileName):
    out_dict={}
    pid=1
    fd=open(fileName,'r')
    for line in fd.readlines():
        regMatch=reg.search(line)
        if regMatch:
            out_dict['pid'+str(pid)]=regMatch.group(1),regMatch.group(2)
            pid=pid+1
    print "==>",out_dict
    return out_dict

p=get_pid('showInventory.txt')
print '-'*50
print " PID Details"
print '-'*50
print ' PID     PID disc   Version'
print '-'*50
for k,v in p.items():
    print '%s    %s    %s'%(k,v[0],v[1])

print '-'*50