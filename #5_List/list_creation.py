# In python, list size can always be dynamic (i.e list ko size badna or ghatna sakcha).. no need to be worry of creating dynamic size like in C & C++
# lists are mutable (meaning that, values or items in the list can be changed or updated)

# Syntax 1 : for Creating empty list in python
first_list = []
print('Type of first_list is :', type(first_list))

# Example 1 :
# Create a list using []
a = [1, 2, 8, 7, 6]

# Print the list using print() function
print(a)


# Syntax 2 : for creating empty list in python
second_list = list()
print('Type of second_list is :', type(second_list))


# Example 2 :
for i in range(4, 15, 2):
	second_list.append(i)

print(second_list)


# We can create a list with items of different types
c = [47, "Hitman", False, 6.9]
print(c)


