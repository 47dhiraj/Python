# Syntax of list comprehension

# SYNTAX 1 ==> [expression for item in list]
# the above syntax means :
# for item in list:
#         expression


# SYNTAX 2 ==>    [ expression for item in list if conditional ]
# the above syntax means :
# for item in list:
#     if conditional:
#         expression


# Example 1:
backpack = ["pizza slice", "button", "pizza slice", "fishing pole", "pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]
print(backpack)

backpack[:] = [item for item in backpack if item != "pizza slice"]
print(backpack)


# Example 2:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)

newlist = [x for x in fruits if "apple" in x]
print(newlist)

# Example 3:
letters = list(map(lambda x: x, 'human'))
print(letters)

# Example 4:
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)

# Example 5 ==> if else with list comprehension
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]
print(obj)

# Example 6 ==> Nested IF with List Comprehension
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

