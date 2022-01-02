# The filter() function in Python takes in a function and a list as arguments.
# The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.


# Example 1: program to filter out only even items from the list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))             # filter function le object return garcha so teslai list ma convert garna ko lagi typecasting gareko ho
print(new_list)


# Example 2 : program to filter the elements which are odd numbers
myList = [10, 25, 17, 9, 30, -5]
myList2 = list(filter(lambda n: n % 2 != 0, myList))
print(myList2)



