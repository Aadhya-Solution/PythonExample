def word_mixer(org_list):
    new_list = []
    org_list.sort()
    org_sort_list = org_list
    print(org_sort_list)
    while len(org_sort_list) > 5:
        ele=org_sort_list[-5]
        org_sort_list.pop(-5)
        new_list.append(ele)
        ele = org_sort_list[0]
        org_sort_list.pop(0)
        new_list.append(ele)
        ele = org_sort_list[-1]
        org_sort_list.pop(-1)
        new_list.append(ele)
    return new_list

st=input("Enter The String:")
st_list = st.split()
temp_list=[]
for each_index in range(len(st_list)):
    if len(st_list[each_index])<=3:
        temp_list.append(st_list[each_index].lower())
    elif len(st_list[each_index])>=7:
        temp_list.append(st_list[each_index].upper())
    else:
        temp_list.append(st_list[each_index])

new_list = word_mixer(temp_list)
for i in new_list:
    print(i,end=" ")