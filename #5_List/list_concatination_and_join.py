#list concatination

# Example 1 : using + operator
list1 = [1, 2]
list2 = [3, 4]
list3 = list1 + list2
print(list3)


# Example 2: using append() method
list4 = [1, 3, 5, 7, 9]
list5 = [2, 4, 6, 8, 10]

for i in list5 :
    list4.append(i)
print(list4)


# Example 4 : using extend() method
test_list3 = [1, 4, 5, 6, 5]
test_list4 = [3, 5, 7, 2, 5]

# using list.extend() to concat
test_list3.extend(test_list4)
print(test_list3)



# Example 5 : concatinating list value with delimiter
string_list = ['1', '2', '3', '4']
print(type(string_list))

string_delimiter = "."
print(type(string_delimiter))

a = string_delimiter.join(string_list)
print(type(a))
print(a)


# Example 6:
import numpy as np

nested_list_a = [[2, 4], [6, 8]]
nested_list_b = [[1, 3],[9, 0]]

c = np.concatenate((nested_list_a, nested_list_b))
print(c)