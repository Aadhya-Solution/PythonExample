def read_file(filename):
    fd=open(filename,'r')
    print fd.read(6)
    print "position :",fd.tell()
    p=fd.readlines()
    print "fd.readlines():",p
    for line in p:
        print "line:>",line.upper()
    fd.close()

def append_file(filename):
    fd=open(filename,'a')
    print "current possition:",fd.tell()
    temp=''
    while True:
        en=raw_input("Enter some:")
        if "$" in en:
            break
        else:
            temp+=en
    fd.write(temp+'\n')

    print "After write --",fd.tell()
    fd.close()

def count_words(file_name):

append_file("abc2.txt")