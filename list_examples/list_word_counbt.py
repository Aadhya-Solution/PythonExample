st=raw_input("String")
st_list=st.split()
dc,wc,alc,spc=0,0,0,0
for i in st_list:
    if i.isdigit():
        dc=dc+1
    elif i.isalpha():
        wc=wc+1
    elif i.isalnum():
        alc=alc+1
    else:
        spc=spc+1
print "-"*30
print "Digit Count:",dc
print "Apla Word Count:",wc
print "Alpha Num Count:",alc
print "Spl Count:",spc