import os
import time

fd=open('123.txt','w')
name=fd.name
fd.close()
print "File Name",name
oldName=name
newName="temp_test22.txt"
fileName='anilTest.py'
folderName="MkFolder"
path="C://Users/rnaraya1/Downloads/pythonClass/"
print "Current dir:",os.getcwd()
currentDir=os.getcwd()
print "Chnage the direct:",os.chdir(path)
print "Current dir after chnageing the path:",os.getcwd()
os.chdir(currentDir)
print "Make Directolry:",os.mkdir(folderName)
time.sleep(20)
print "Change the name:",os.rename(oldName,newName)
time.sleep(20)
print "Remove File :",os.remove(fileName)
time.sleep(20)
print "REmove directory:",os.rmdir(folderName) 



