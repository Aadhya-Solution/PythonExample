import re
detail_dict={}



with open("showHardware.txt") as fd:
    l=fd.readlines()
    for i in l:
        m=re.search(r'ROM:.*Version\s*([\d\.\(\w\)]+)',i)
        if m:
            version=m.group(1)
            detail_dict.update({'version':version})
            print("Version:{}".format(m.group(1)))
        m1=re.search(r'Router.*(\d)\s*day\,\s*(\d+)\s*hours\,\s*(\d+)\s*minutes',i)
        if m1:
            day= m1.group(1)
            hours= m1.group(2)
            min=m1.group(3)
            detail_dict.update({'uptime': {'day':day,'hours':hours,'min':min}})

print(detail_dict)
