# if you need the original list unchanged when the new list is modified, you can use the copy() method.

'''

The problem with copying lists in this way is that if you modify new_list, old_list is also modified.
It is because the new list is referencing or pointing to the same old_list object.

'''

# Example 1:
old_list = [1, 2, 3]
print('Original List :', old_list)

new_list = old_list.copy()

print('Original List :', old_list)
print(new_list)


# Example for Shallow copy ==> it means the any modification in new list won’t be reflected to original list
# Example 2 ==> Copy List Using Slicing Syntax

# shallow copy using the slicing syntax
list = ['cat', 0, 6.7]
print('Original List :', list)

new_list = list[:]                  # copying a list using slicing syntax not with copying method

# Adding an element to the new list
new_list.append('dog')

# Printing new and old list
print('Old List:', list)
print('New List:', new_list)


# # techniques of deep and shallow copy
import copy

# Initializing list
list1 = [ 1, [2, 3] , 4 ]

# all changes are reflected
list2 = list1

# shallow copy - changes to nested list is reflected,
# same as copy.copy(), slicing

list3 = list1.copy()

# deep copy - no change is reflected
list4 = copy.deepcopy(list1)

list1.append(5)
list1[1][1] = 999

print("list 1 after modification:\n", list1)
print("list 2 after modification:\n", list2)
print("list 3 after modification:\n", list3)
print("list 4 after modification:\n", list4)