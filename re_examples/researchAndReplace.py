import os
pat_str ="What"
path="E:/pythonExamles/regEx/reFolder/"
for file1 in os.listdir(path):
    #print file1
    fileName=os.path.join(path,file1)
    #print "==>",fileName
    fl= open(fileName,"r")
    for s in fl.readlines():
        if pat_str in s:
            print "text %s is found in %s"%(pat_str,file1)
        else:
            print "No Man :-("
    fl.close()