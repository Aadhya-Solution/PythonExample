# File: os-example-5.py

import os
def read_file(file):
    fd=open(file,'r')
    for i in fd.readlines():
        print i

for file in os.listdir("inputFile"):
    fpath=os.path.join(os.getcwd(),'inputFile',file)
    #print fpath
    if os.path.isfile(fpath):
        if file.endswith('.txt'):
            print fpath
            read_file(fpath)

## sample.au
## sample.jpg
## sample.wav
## ...
