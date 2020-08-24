f=True
fd=open("file_test.txt",'w')
while f:
    ele=raw_input("Enter the text:")
    fd.write(ele)
    fd.write('\n')
    opt=raw_input("Do you want to continue: yes or no")
    if opt.lower() in ['yes','y']:
        f=True
    else:
        f=False
fd.close()