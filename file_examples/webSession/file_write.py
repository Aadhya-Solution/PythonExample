

#txt,csv,tsv,log,config
#fd=open("FileName/abs filePath",mode)
#mode--> write (w) read(r) append (a)
#        write+read (w+)  read+write(r+)  write+read(a+)

fd=open('test1.txt','w')
while True:
     st=input("Enter Something:")
     fd.write(st+"\n")
     opt=input("Do you continue or not:")
     if opt in ['yes','y']:
         pass
     else:
         break
fd.close()
