def get_rev_word(each_word):
    st=''
    l=len(each_word)
    while l>0:
        st=st+each_word[l-1]
        l=l-1
    return st

def do_revers_line(line):# This is Mango
    list_line=line.split() #['This','is','Mango']
    res_str=''
    for each_word in list_line:
        st=get_rev_word(each_word)#shashi--->ihsahs
        res_str=res_str+' '+st
    return res_str.strip()

def read_file(filename):
    import sys
    try:
        fd=open(filename,'r')
    except IOError:
        print("File is not Exist, Plz give proper file")
        sys.exit(1)
    fd1=open('reversed.txt','w')
    line_list=fd.readlines()
    for eachLine in line_list:
        revers_line=do_revers_line(eachLine)
        fd1.write(revers_line)
        fd1.write("\n")
    fd.close()
    fd1.close()

read_file('abc.txt')
print("File Operation Done")