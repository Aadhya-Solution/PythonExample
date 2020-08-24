import re
reg=re.compile(r'\s*System\s*Manufacturer:\s*(\w+)')
reg_install_date=re.compile(r'Original\s*Install\s*Date\s*:\s*(.*)')
reg_system_boot_date=re.compile(r'System\s*Boot\s*Time\s*:\s*(\d{1,2}\/\d{1,2}\/\d{2,4})\s*,.*')

def get_sysinfo(fileName):
    out_dict={}
    fd=open(fileName,'r')
    for eachline in fd.readlines():
        regMatch=reg.search(eachline)
        regMatch_install=reg_install_date.search(eachline)
        regMatch_boot=reg_system_boot_date.search(eachline)
        if regMatch:
            out_dict.update({'Manufacturer':regMatch.group(1)})
        if regMatch_install:
            out_dict.update({'Installed Date':regMatch_install.group(1)})
        if regMatch_boot:
            out_dict.update({'Boot time':regMatch_boot.group(1)})
    return out_dict


if __name__ == '__main__':
    p=get_sysinfo('systeminfo.txt')
    print "-"*50
    print "System Details "
    print "-"*50
    for k,v in p.items():
        print k,v
    print "-"*50