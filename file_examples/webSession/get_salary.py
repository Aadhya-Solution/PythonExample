import re
with open("employee_details.txt") as fd:
    l=fd.readlines()
    employee_list=[]
    for each_line in l:
        m = re.search('(\w+)\s*\d{2}\s*\w+\s*\d+\/\d+\/\d+\s*(\d+)', each_line)
        if m:
            name= m.group(1)
            salary=m.group(2)
            employee_list.append({'name':name,'salary':salary})

for i in employee_list:
    print(i)