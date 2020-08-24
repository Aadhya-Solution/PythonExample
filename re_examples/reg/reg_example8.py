import re

st="Name: Shiva DOB:10/05/1990"
r=re.search("(\d{1,2})\/(\d{1,2})\/(\d{2,4})",st)
if r:
    print "Found",r.group(1),r.group(2),r.group(3)
else:
    print "Not found"
    
print "With Complie"

reg=re.compile("Name:\s+(\w+)\s+DOB:(\d{1,2})\/(\d{1,2})\/(\d{2,4})")

reg_match=reg.search(st)
if reg_match:
    print "Found",reg_match.group(1),reg_match.group(2)
else:
    print "Npot matched"
print "Gorups:",reg_match.groups()