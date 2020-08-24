import re
import os

reg=re.compile(r'^\s*ROM\s*:\s*[\w\s]+\s*,\s*Version\s*([\d\.\(\)\w]+).*')
reg_up=re.compile(r'\s*Router\s*uptime\s*is\s*(\d+\s*day)\s*,\s*(\d+\s*hours)\s*,\s*(\d+\s*minutes)')
reg_img=re.compile(r'\s*System\s*image\s*file\s*is\s*\"disk\d+:\s*([\w\-\.]+)\"')
def get_hardware(fileName):
    out_dict={}
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
    print "===>",out_dict
    return out_dict

def print_file(p,fileName):
    fd=open('hardware_report.txt','a')
    fd.write('='*50+'\n')
    fd.write(" Hardware Details"+'\n')
    fd.write("FileName:"+os.path.split(fileName)[1]+"\n")
    fd.write('='*50+'\n')
    for k,v in p.items():
        fd.write('%s    %s\n'%(k,v))
    fd.write('-'*50+'\n')
    fd.close()

def print_report(filename):
    p=get_hardware(filename)
    print_file(p,filename)

#print_report('showHardware.txt')

import os
for eachfile in os.listdir('show_hardware'):
    currentPath=os.getcwd()
    temp_path=os.path.join('show_hardware',eachfile)
    filePath=os.path.abspath(temp_path)
    print_report(filePath)
