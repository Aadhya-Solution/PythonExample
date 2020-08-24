l,w,d,sl=0,0,0,0
dc=0
while 1:
    fileName=raw_input("File name:")
    try:
        fd=open(fileName,'r')
        break
    except IOError,e:
        print "Error:%s"%(e)
        print "Please eneter Proper FileName"
fileList=fd.readlines()
l=len(fileList)
for i in fileList:
    print i
    eachLine=i.split()
    print "After Split:",eachLine
    for j in eachLine:
        if j.isdigit():
            d=d+1
            dc=dc+len(j)
        elif j.isalnum():
            w=w+1
    if len(eachLine)==0:
        sl=sl+1

print "Total Line:%d\nTotal Words:%d\n" \
      "Total Digit:%d\nTotal blank Line%d"%(l,w,d,sl)
print "Total digits:%d"%(dc)