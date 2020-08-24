nword=raw_input("Enter the line")
cd=0
wc=0

wlist=nword.split()
for each_word in wlist:
    if each_word.isdigit():
        cd=cd+1
    if each_word.isalpha():
        wc=wc+1
print "Total numb of Word :",wc
print "Total numb of digit:",cd