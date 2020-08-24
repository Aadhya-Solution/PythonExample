nword=raw_input("Enter the line")
c=0
wlist=nword.split()
for each_word in wlist:
    if each_word == 'The':
        c=c+1
print "Word count the :",c