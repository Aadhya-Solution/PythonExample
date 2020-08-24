fd =open("test5.txt",'w')
l=['tthis is\n','going to\n','i am in blore\n']
fd.writelines(l)
fd.close()