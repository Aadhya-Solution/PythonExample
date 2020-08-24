import re
reg_ipv6=re.compile(r'\s*Link-local\s*IPv6\s*Address\s*[\.\s]*:\s*([\w\:%]+)')
reg_ipv4=re.compile(r'\s*IPv4\s*Address[\.\s]+\:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

reg_ipv4=re.compile(r'\s*IPv4\s*Address\s*[\.\s]*:\s*([\w\.]+)')
reg_ipSubnet=re.compile(r'Subnet Mask . . . . . . . . . . . : 255.255.255.0')
reg_gateway=re.compile(r'Default Gateway . . . . . . . . . : 192.168.1.1')

def getInfo(fileName):
    fd=open(fileName,'r')
    out_dict={}
    for eachLine in fd.readlines():
        regMatch_ipv4=reg_ipv4.search(eachLine)
        regMatch=reg_ipv6.search(eachLine)
        if regMatch_ipv4:
            out_dict.update({'ipv4':regMatch_ipv4.group(1)})
        if regMatch:
            out_dict.update({'ipv6':regMatch.group(1)})
    return out_dict

p=getInfo('show_ipconfig.txt')
fd1=open("Report_ipconfig.txt",'w')
fd1.write('='*50+'\n')
fd1.write('        IP Details      \n')
fd1.write('='*50+'\n')
for k,v in p.items():
    fd1.write(k+'   '+v+'\n')
fd1.write('='*50+'\n')
fd1.close()