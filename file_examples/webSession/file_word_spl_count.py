def get_word_spel_count(file_name):
    fd=open(file_name,'r')
    l=fd.readlines()#['Shiva is having 6000 $\n', 'He is going 8u98II&& \n' , " "]
    dc=0
    wc=0
    swc=0
    blk_line=0
    count_dict={}
    for j in l:
        for i in j.split():
            if i.isdigit():
                dc=dc+1
            elif i.isalpha():
                wc=wc+1
            else:
                swc=swc+1
        if j.isspace():
            blk_line=blk_line+1

    #['Shiva is good\n', 'He is going\n']
    fd.close()
    #
    count_dict.update({'digit_count':dc,"alpha_count":wc,"special_count":swc,'blank_lines':blk_line})
    return count_dict
l=['test1.txt','test2.txt','test3.txt']
wc_list=[]
for i in l:
    dict_count =get_word_spel_count(i)
    print("File:{}--{}".format(i,dict_count))




#
# File Name     WC      SWC   Dc  Blck Line
# test1.txt     9        3     2    2
# test2.txt     8        2     2    1



