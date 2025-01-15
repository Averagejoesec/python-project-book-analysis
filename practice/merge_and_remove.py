list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

combined_list = []
for i in list1:
    if i not in list2:
        combined_list.append(i)
    else:
        continue
for i in list2:
    if i not in list1:
        combined_list.append(i)
    else:
        continue
print(combined_list)