str_line=raw_input("Enter line:")
str_list=str_line.split()
final_str=''
for eachWord in str_list:
    str_len=eachWord.__len__()
    st=''
    while str_len>0:
        st=st+eachWord[str_len-1]
        str_len=str_len-1
    final_str=final_str+' '+st

print "Given line:",str_line
print "Reversed Line:",final_str