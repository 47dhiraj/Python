# One way ==> Only getting unique elements without preserving the order or the elements inside list

# Example 1 : Using python set() method
list1 = [40, 20, 10, 30, 40]
print("List 1 at initial : ", list1)

unique_set = set(list1)                 # finds unique element but doesn't preserve the order of element
unique_list = list(unique_set)

print('Unique List : ', unique_list)

# Example 2 : using numpy.unique() method ==> it also doesn't preserve the order of element inside list.. it just sort the unique elements in the ascending order
import numpy as np
list2 = [40, 20, 10, 30, 40, 30]
# print(np.unique(list2))
# x = np.array(list2)
# print(np.unique(x))




# Best way : finding unique elements in the list & also preserving the order of elements in the list

# Example 1 : Using manual traversal
unique_list = []
list3 = [40, 20, 10, 30, 40, 30]

for x in list3:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)
