import re
pat=r'\s*Name:\s*(\w+)\s*'
pat2=r'\s*cont\s*:\s*(\d+)\s*'

def getData(data):
    l=[]
    for eline in data:
        m=re.match(pat,eline)
        m1=re.match(pat2,eline)
        if m:
            name=m.group(1)
        elif m1:
            cont=m1.group(1)
            l.append({'name':name,'cont':cont})
    return l

def readFile(filename):
    fd=open(filename,'r')
    l=fd.readlines()
    data=getData(l)
    fd.close()
    return data
def genReport(data):
    line="="*20
    h="Std Details".center(20)
    print line
    print h
    print line
    for i in data:
        print "{}   {}".format(i['name'],i['cont'])
    print line


data=readFile('re_std_input2.txt')
genReport(data)
