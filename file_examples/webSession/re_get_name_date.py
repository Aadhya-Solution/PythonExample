import re

fd=open("std_report.txt",'r')
l=fd.readlines()
for each_line in l:
    m = re.search(r'Name\:\s*(\w+).*(\d{2}\/\d{2}\/\d{2,4})', each_line)
    if m:
        name=m.group(1)
        date=m.group(2)
        print("Name:{} Date:{}".format(name,date))

fd.close()
