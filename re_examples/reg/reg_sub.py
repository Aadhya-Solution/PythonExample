import re 
str1 = 'purple alice.b--abc@gmail.com, blah monkey bob@gamil.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yahoo.com', str1)
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher



#str=" dob: 10/03/2016    loc : BTM      Joined: 12/03/2017"
#out="dob: 2016      loc: BTM     Joind: 2017"