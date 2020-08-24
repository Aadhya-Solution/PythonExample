n=input("Enter Std size:")
std_list=[]
for i in range(1,n+1):
    print("Enter {}st Std Details".format(i))
    std_name = input("{}st Std Name:".format(i))
    std_age = input("{}st Std Age:".format(i))
    std_loc = input("{}st Std Loc:".format(i))
    std_list.append({'name':std_name,
                     'age':std_age,
                     'loc':std_loc})
print("Std Details update Done")
line="="*30
header="|{}|{}|{}|".format("Name".center(10),"Age".center(10),'Loc'.center(10))
print(line)
print(header)
print(line)
for each_std in std_list:
    print("|{}|{}|{}|".format(each_std['name'].center(10),each_std["age"].center(10),each_std['loc'].center(10)))
print(line)