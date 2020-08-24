fd=open("test1.txt",'r')
fd1=open("test2.txt",'r')
fd2=open("test_merge.txt",'w')
fd2.writelines(fd.readlines())
fd2.writelines(fd1.readlines())
fd.close()
fd1.close()
fd2.close()
'''

read write append
merge 
next 


Number of lines in file and 
first and last word should be in upperlatter
tt his is
go ing to
i am in blore
==>
TT his IS
GO ing TO
I am in BLORE

Merge n Numer of files 
5
  if test1.txt, test2.text...:
      merge.txt --> 
      
file1.txt
feil2.txt
final.txt
     f1_l1
     f2_l1
     f1_l2
     f2_l2
     f1_l3
     f2_l3
     
     
     
+========================
       Std Detail 
+=========================
Name 
Age
CLoc
Adrress
==========================

=================================================
               Std Details 
=================================================
Name        Age      Loc      Address      Result
=================================================
Rama        20       BTM       BTM        pass

================================================

1
file1.txt
Shiva is going 
this is mango

===>rev.txt
avihS  si   gniog
siht   is  ognam

2. 
file1.txt
Shiva is going 
this is mango

===>rev.txt
going is Shiva
mango is this
'''