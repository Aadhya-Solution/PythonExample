ele=raw_input("Eenter String:")
wc,dc,sc=0,0,0
elist=ele.split()
for e in elist:
    if e.isdigit():
        dc=dc+1
    elif e.isalnum():
        wc=wc+1
    else:
        sc=sc+1
print "Words:",wc
print "Digit Count:",dc
print "Spe Count:",sc
