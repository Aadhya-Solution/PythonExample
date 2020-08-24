import pdb
while True:
	try:
		n=input('Enter size of the list:')
		break
	except:
		print("Please provide proper input int value")
l=[]
pdb.set_trace()
for i in range(n):
    ele=input("Enter the list element:")
    l.append(ele)

print("list",l)
big=l[0]
for i in range(1,len(l)):
	print(i,"--",l[i])
	if big<l[i]:
		big=l[i]

print("Biggest element:",big)