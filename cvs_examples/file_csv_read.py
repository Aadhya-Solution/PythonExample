fd = open('persons.csv','r')

l = fd.readlines()
for i in l:
    name,job = i.split(",")
    print name,job

fd.close()