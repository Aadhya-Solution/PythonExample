import os

for eachFile in os.listdir('inputFile'):
    fpath=os.path.join(os.getcwd(),'inputFile',file)
    #print fpath
    if os.path.isfile(fpath):
        print file # disply all the files