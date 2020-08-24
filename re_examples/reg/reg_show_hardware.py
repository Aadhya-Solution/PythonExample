import re

reg=re.compile(r'^\s*ROM\s*:\s*[\w\s]+\s*,\s*Version\s*([\d\.\(\)\w]+).*')
reg_up=re.compile(r'\s*Router\s*uptime\s*is\s*(\d{1,2}\s*day)\s*,\s*(\d+\s*hours)\s*,\s*(\d+\s*minutes)')
reg_img=re.compile(r'\s*System\s*image\s*file\s*is\s*\"disk\d+:\s*([\w\-\.]+)\"')
def get_hardware(fileName):
    out_dict={}
    pid=1
    fd=open(fileName,'r')
    for line in fd.readlines():
        regMatch=reg.search(line)
        regMatch2=reg_up.search(line)
        regMatch3=reg_img.search(line)
        if regMatch:
            out_dict['version']=regMatch.group(1)
        if regMatch2:
            uptime=regMatch2.group(1)+regMatch2.group(2)+regMatch2.group(3)
            out_dict['Up Time']=uptime
        if regMatch3:
            img=regMatch3.group(1)
            out_dict['img']=img
    return out_dict


p=get_hardware('/home/shashi/PycharmProjects/pythonExamples/pythonExamples/showHardware.txt')
print '-'*50
print " Interface Details"
print '-'*50
print ' Int Details    Status'
print '-'*50
for k,v in p.items():
    print '%s    %s'%(k,v)
print '-'*50
