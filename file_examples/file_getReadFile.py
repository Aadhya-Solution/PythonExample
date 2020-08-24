import os
import time
folderPath=os.path.abspath('inputFile')
outputPath=os.path.join(folderPath,'output')
targetFileName='target_'+str(time.time())+'.txt'
targetFile=os.path.join(outputPath,targetFileName)
fd1=open(targetFile,'w')
for eachFile in os.listdir(folderPath):
    filePath=os.path.join(folderPath,eachFile)
    if not os.path.isdir(filePath):
        fd=open(filePath,'r')
        for eachLine in fd.readlines():
            fd1.write(eachLine)
        fd.close()
fd1.close()
