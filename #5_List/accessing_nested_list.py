# Example 1:

nested_list = [[2, 4], [6, 8, 10], [36, 47, 58, 69]]

empty_list=[]

for i in nested_list:
  for j in i:
    empty_list.append(j)

print(empty_list)