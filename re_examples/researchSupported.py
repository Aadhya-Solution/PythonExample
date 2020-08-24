import os
import re

def searchSupUnSup(parFolder,Path,lineSearch):
    mlSupported =[]
    mlunSupported = []
    unsupported_cmds=[]
    os.chdir(Path)
    for file in os.listdir(parFolder):
        print "Dir name",file
        listDir.append(file)
    os.chdir("ASR9k")
    cwd = os.getcwd()
    print "file", cwd
    for eachFolder in listDir:
        os.chdir(eachFolder)
        cwd = os.getcwd()
        print "Path of %s is %s"%(eachFolder,cwd)
        folderPath.append(cwd)
        os.chdir(os.pardir)
    k=0
    for eachFolder2 in folderPath:
        k=k+1
        print "folder name :",eachFolder2
        os.chdir(eachFolder2)
        for file in os.listdir(eachFolder2):
            str=""
            print "file %s in %s Dir Path "%(file,eachFolder2)
            if file == "supported_cmds":
                #list_line = []
                fl= open(file,"r")
                str="" 
                for s in fl.readlines():
                    
                    p = re.compile("(self)(\.)(supported_cmds|unsupported_cmds)\s+?(=)\s+?(\[).*?", re.IGNORECASE|re.DOTALL)
                    m = p.search(s)
                    if  m:
                        #list_line = []
                        flag = True
                    if "self.supported_cmds = [(re.compile" in s:
                        flag = False
                        break
                    if flag == True :
                        #list_line.append(s.strip())
                        #print "----->", s.strip()
                        m2=re.search(r"(.*)\)?\s*\,?\s*\#(.*)",s.strip())
                        if m2:
                           s=m2.group(1)
                        m3=re.search(r"^\#(.*)",s.strip())
                        if not m3:
                            str=str+s.strip()
                        
                        
                    #for i in list_line:
                    #    str=str+i            
                               
                fl.close()
            ##if file == "unsupported_cmds":
            ##    #list_line = []
            ##    fl= open(file,"r")
            ##    str="" 
            ##    for s in fl.readlines():
            ##        p1= re.match(r"self.unsupported_cmds\s*\=\s*\[^",s)
            ##        if p1:
            ##            print "Here i am in break "
            ##            break
            ##        p = re.compile("(self)(\.)(unsupported_cmds)\s+?(=)\s+?(\[).*?", re.IGNORECASE|re.DOTALL)
            ##        m = p.search(s)
            ##        if  m:
            ##            #list_line = []
            ##            flag = True
            ##        if "self.unsupported_cmds = [re.compile(" in s:
            ##            flag = False
            ##            break
            ##        if flag == True :
            ##            #list_line.append(s.strip())
            ##            print "----->", s.strip()
            ##            m2=re.search(r"(.*)\)?\s*\,?\s*\#(.*)",s.strip())
            ##            if m2:
            ##               s=m2.group(1)
            ##            m3=re.search(r"^\#(.*)",s.strip())
            ##            if not m3:
            ##                str=str+s.strip()
            ##            
            ##            
            ##        #for i in list_line:
            ##        #    str=str+i            
            ##                   
            ##    fl.close()
                 
            str=str.replace("self.","",1)
            str=str.strip()
        #print "Supported string ",str
            #print "str :",str[-1]
            #print "\n\n\n---"
            #print" str ===\n",str,"\n\n++++"
            exec(str)
        #print "Supported string ",supported_cmds
            
            #unsupported_cmds = [(re.compile(regex[0],re.IGNORECASE),regex[-1]) for regex in unsupported_cmds]
            try:
                supported_cmds = [(re.compile(regex[0],re.IGNORECASE),regex[-1]) for regex in supported_cmds]
                #unsupported_cmds = [re.compile(regex,re.IGNORECASE) for regex in unsupported_cmds]
                mlunSupported.append(supported_cmds)
            except ValueError:
                pass
            #for i in supported_cmds:
            #    print i
    
    c=0  
    for i in mlunSupported:
        c=c+1
        print i
    print "Total number of foders ",k
fileOut =''
filePath = ''
#F:\ciscoProject\sox\Assigemnet
filename = "Newfile.txt"
folderPath=[]
cwd = os.getcwd()
print "1", cwd
list1 =[]
listDir=[]
text="router-id"
Path="F:\ciscoProject\sox\\"
parFolder="ASR9k"
lineSearch ="router-id"
searchSupUnSup(parFolder,Path,Path)


    #if os.path.isdir(file) == True:
    #    print "file:2",file
    #    filepath=os.chdir(file)
    #    print "file path is ",filepath
        #fileOut=filePath+file.rstrip('\n\r ')
        #fl= open(file,"r")
        #for s in fl.readlines():
        #    if text in s:
        #        print "text %s is found in %s"%(text,file)
        #
        #fl.close()
#for eachInFolder in listDir:
    #os.chdir(eachInFolder)
    #
    #print "file %s in %s Dir"%(eachInFolder,listDir[eachInFolder])
    #fl= open(eachInFolder,"r")
    #for s in fl.readlines():
    #    print s
    #    if text in s:
    #        print "text is found in %s and in %s dir"%(eachInFolder,listDir[eachInFolder])
    #fl.close()
    # go back up to parent directory 
    #os.chdir(os.pardir)
    