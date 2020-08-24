line=raw_input("Enter the line:")
word_list=line.split()
print word_list
n=len(word_list)
wc,dc,sc=0,0,0
for each_word in word_list:
    if each_word.isdigit():
        dc=dc+1
    elif each_word.isalpha():
        wc=wc+1
    elif each_word.isspace():
        sc=sc+1
if len(word_list)==0:
    print "Empty line"
else:
    print "Total Digits:",dc
    print "Total words",wc
    print "Total space:",sc
