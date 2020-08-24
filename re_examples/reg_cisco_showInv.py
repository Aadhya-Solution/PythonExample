import re
reg_pid=re.compile(r'^\s*PID\s*:\s*([\w\-\/]+)\s*.*SN:\s*(\w+)')
reg_slot=re.compile(r'^\s*NAME\s*:\s*\"([\w\_\-\/\:\s]+)\"\s*\,\s*.*')
def get_pid(fileName):
    out_dict={}
    slot_flag = False
    fd=open(fileName,'r')
    for line in fd.readlines():
        reg_match_slot = reg_slot.search(line)
        if reg_match_slot:
            slot_flag = True
            slot = reg_match_slot.group(1)
        reg_match=reg_pid.search(line)
        if reg_match and slot_flag:
            out_dict[slot]=reg_match.group(1),reg_match.group(2)
            slot_flag = False
    print out_dict
    return out_dict

p=get_pid('/home/shashi/PycharmProjects/pythonExamples/pythonExamples/showInventory.txt')
print '-'*50
print " PID Details"
print '-'*50
print ' PID     PID disc   Version'
print '-'*50
for k,v in p.items():
    print '%s    %s    %s'%(k,v[0],v[1])

print '-'*50