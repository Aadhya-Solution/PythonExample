import re
pat=r'Name:\s*(\w+)\s*Age:\s*(\d{1,2})\s*Loc:\s*(\w+)'

def getData(line):
    m=re.match(pat,line)
    if m:
        name=m.group(1)
        loc=m.group(3)
        return {'name':name,'loc':loc}
    else:
        return None
def readFile(filename):
    fd=open(filename,'r')
    l=fd.readlines()
    report=[]
    for eline in l:
        data=getData(eline)
        if data:
            report.append(data)
    fd.close()
    return report
def genReport(data):
    line="="*20
    h="Std Details".center(20)
    print line
    print h
    print line
    for i in data:
        print "{}   {}".format(i['name'],i['loc'])
    print line


data=readFile('re_std_input1.txt')
genReport(data)
