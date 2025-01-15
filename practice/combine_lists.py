list1 = [5, 3, 8, 6, 3]
list2 = [7, 2, 5, 9, 8]

def combine_lists(list1, list2):
    combined_lists = list1 + list2
    combined_lists.sort()
    combined_lists = list(dict.fromkeys(combined_lists))
    return combined_lists

print(combine_lists(list1, list2))

# Solution method
# Combine, remove duplicates, and sort using a loop
unique_list = []
for item in list1 + list2: # Concatenate lists
    if item not in unique_list:
        unique_list.append(item)

unique_list.sort() # Sort the unique list
print(unique_list)