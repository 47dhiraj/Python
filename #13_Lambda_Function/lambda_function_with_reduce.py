# The reduce() function in Python takes in a function and a list as an argument.
# The function is called with a lambda function and an iterable and a new reduced result is returned.
# This performs a repetitive operation over the pairs of the iterable.

from functools import reduce

# Example 1 :
li = [5, 8, 10, 20, 50, 100]
sum = reduce(lambda x, y: x + y, li)
print(sum)


# Example 2 : reduce to compute maximum element from list
lis = [1, 3, 5, 6, 2, ]
print("The maximum element of the list is : ", end="")
print(reduce(lambda a, b: a if a > b else b, lis))

