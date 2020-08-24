def count_word_digt_line(fileName):
    fd=open(fileName,'r')
    nl,nw,wd,empt,spc=0,0,0,0,0
    file_list=fd.readlines()
    nl=file_list.__len__()
    for eachLine in file_list:
        list_word=eachLine.split()
        for eword in list_word:
            if eword.isdigit():
                wd=wd+1
            elif eword.isalnum():
                nw=nw+1
            else:
                print eword
                spc=spc+1
        if eachLine.isspace():
            empt=empt+1
    return nl,nw,wd,empt,spc


if __name__ == '__main__':
    nl,nw,wd,em,spc=count_word_digt_line('file_count')
    print "Num Lines:",nl
    print "Num Word:",nw
    print "Num Digit:",wd
    print "Empty line",em
    print "Sp word",spc