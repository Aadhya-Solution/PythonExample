import re

reg=r'([\w\.\-\:\/]+)\s*(up|down)\s*(up|down).*'

def reg_match_int(fileName):
    out_dict={}
    fd=open(fileName,'r')
    for line in fd.readlines():
        regMatch=re.search(reg,line)
        if regMatch:
            out_dict[regMatch.group(1)]=regMatch.group(2)
    return out_dict


p=reg_match_int('/home/shashi/PycharmProjects/pythonExamples/pythonExamples/showInterface.txt')
print '-'*50
print " Interface Details"
print '-'*50
print ' Int Details    Status'
print '-'*50
for k,v in p.items():
    print '%s    %s'%(k,v)

print '-'*50
