import re

# reg=re.search(r'([\w\.\-\:\/]+)\s*(up|down)\s*(up|down).*')

def reg_match_int(fileName):
    out_dict={}
    fd=open(fileName,'r')
    for line in fd.readlines():
        regMatch=re.search(r'([\w\.\-\:\/]+)\s*(up|down)\s*(up|down).*', line)
        if regMatch:
            intf= regMatch.group(1)
            admin_status = regMatch.group(2)
            out_dict[intf]=admin_status
    return out_dict


p=reg_match_int('showInterface.txt')
print(p)
print('-'*50)
print(" Interface Details")
print('-'*50)
print(' Int Details    Status')
print('-'*50)
for k,v in p.items():
    print('%s    %s'%(k,v))

print('-'*50)
