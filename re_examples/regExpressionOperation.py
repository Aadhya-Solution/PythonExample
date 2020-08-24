import properties

from properties import filePath


def readfile(filename):
    f=open(filename,"r")
    text=f.read()
    f.close()
    print text

def writeFile(filename,content):
    f=open(filename,"w")
    f.write(content)
    f.close()

print " This is the reg expression file handling program"
print '========================================='
print '1. Display file'
print '2. search for the element'
print '3. replace the element'
print '4. remove the content for the file'
print '5. find the details fo the file'
print '6. find the accurnece of the spesific elemet in the file'
print '7. Exit from the operation'
print

select_choice = 0
while true:
    if select_choice==1:
        print 'Display file :'
        readfile(filePath+filename.rstrip('\n\r '))
    elif select_choice==2:
        search_ele = raw_input('Enter the elementy to search:')


