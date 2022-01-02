'''
A set is an auto sorted collection of items.
A set object doesnot support indexing i.e indexing garna mildaina.
Every set element is unique (no duplicates) and must be immutable (cannot be changed).
However, a set itself is MUTABLE. We can add or remove items from it.
'''

# Syntax for creating empty sets
# a = set()
# print(a)
# print(type(a))


# Example 1:
b = {1, 3, 4, 5, 1}             # syntax for creating non-empty sets i.e using curly brace
print(type(b))
print(b)


# Example 2 : set of mixed datatypes
# my_set = {1.0, "Hello", (1, 2, 3)}
# print(type(my_set))
# print(my_set)


# Example 3 : set cannot have duplicates
my_set = {1, 2, 3, 4, 3, 2}             # duplicate vako data lai automatic hatayera.. single times or ek choti matra data rakhcha
print(my_set)











# NOTE
# Important: This below syntax will create an empty dictionary and not an empty set
# z = {}
# print(z)
# print(type(z))


