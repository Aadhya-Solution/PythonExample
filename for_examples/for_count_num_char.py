st="gooogle.com"
out_dict={}
for i in st:
    if out_dict.has_key(i):
        out_dict[i]=out_dict[i]+1
    else:
        out_dict[i]=1
print(out_dict)