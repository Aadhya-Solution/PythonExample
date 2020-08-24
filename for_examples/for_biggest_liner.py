l=input('Enter interger list:')#[12,23,34,1]
print("list",l)
big=l[0]
for i in range(1,len(l)):#[1,2,3,4]
	print(i,"--",l[i])
	if big<l[i]:
		big=l[i]

print("Biggest element:",big)