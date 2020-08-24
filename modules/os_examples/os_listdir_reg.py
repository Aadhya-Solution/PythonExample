# File: os-example-5.py
import re
import os

regComp=re.compile(r'(\d+\.\d+\.\d+\.\d+).*')
def read_file(file):
    fd=open(file,'r')
    dictp={}
    iplist=[]
    for i in fd.readlines():
        p=regComp.search(i)
        if p:
            iplist.append(p.group(1))
    dictp.update({'file':file,'ips':iplist})
    return dictp
l=[]
out=[]
for file in os.listdir("inputFile"):
    fpath=os.path.join(os.getcwd(),'inputFile',file)
    #print fpath
    if os.path.isfile(fpath):
        if file.endswith('.txt'):
            print "-->",fpath
            out.append(read_file(fpath))

print "=="*10
for eachFile in out:
    for file,ips in eachFile.items():
        print file,"==",ips
## sample.au
## sample.jpg
## sample.wav
## ...
