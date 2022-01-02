# The map() function in Python takes in a function and a list.
# The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.


# Example 1 : program to double each item in the list using map() function.
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))           # map function le map object return garcha so teslai list ma convert garna ko lagi typecasting gareko ho
print(new_list)

# Example 2 : Program to half each item in the list uisng map() function
myList = [10, 25, 17, 9, 30, -5]
myList2 = list(map(lambda n: n/2, myList))              # map function le map object return garcha so teslai list ma convert garna ko lagi typecasting gareko ho
print(myList2)

