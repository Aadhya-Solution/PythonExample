s=input("Enter String:")
nl=len(s)
for i in range(len(s)):
    temp=""
    for j in s[:i+1]:
        temp=temp+' '+j
    print(" "*(nl-1)+temp+" "*(nl-1))
    nl=nl-1
"""
'      S     '
'     S H    '
'    S H A   '
'   S H A S  '
'  S H A S H '
' S H A S H I'
"""