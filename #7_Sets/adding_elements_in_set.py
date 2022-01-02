# Adding elements in set

my_set = {1, 3}
print(type(my_set))
print(my_set)

# my_set[0]             # TypeError: 'set' object does not support indexing


# add an element
# my_set.add(2)         # .add() method takes exactly 1 argument to be added, not more than one argument
# print(my_set)
# print(type(my_set))



# add multiple elements
# my_set.update([2, 5, 4])
# print(my_set)



# add list and set
my_set.update([2, 5, 4, 6], {1, 7, 6, 8})
print(my_set)




