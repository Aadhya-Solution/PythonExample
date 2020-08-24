import re

def get_int_ip(file_name):
    ip_dict ={}
    fd=open(file_name,'r')
    for i in fd.readlines():
        matchObj = re.search("([\w\.\-\/\:]+)\s*(up|down)\s*(up|down)\s*\w*\s*([\d\.\/]+)",i)
        if matchObj:
            intf=matchObj.group(1)
            ip=matchObj.group(4)
            ip_dict.update({intf:ip})
    return ip_dict

def gen_report(data):
    fd=open("ip_report.txt",'w')
    fd.write("="*30+"\n")
    fd.write("Intface                    IP\n")
    fd.write("="*30+"\n")
    for intf, ip in data.items():
        str_rp ="{}                        {}\n".format(intf,ip)
        fd.write(str_rp)
    fd.write("="*30+"\n")
    fd.close()

data= get_int_ip("showInterface.txt")
gen_report(data)