# tuples are immutable (meaning they cannot be changed)
# Tuple size can be dynamic in python
# we can create a tuple with items of different types

# example 1 :
emptyTuple = ()
print(type(emptyTuple))

# example 2:
emptyTuple = tuple()
print(type(emptyTuple))


# For checking if the tuple is empty
if len(emptyTuple) == 0:
	print('Tuple is empty.')

# Example 1 : tuple with single value

a = (2,)              # () (i.e small braces) tuple ho vanera janauncha so comma diyena vani (2) lai integer ho vanera janauncha
print(a)
print(type(a))

b = (2)
print(b)
print(type(b))

# Example 2:
t = (1, 2, 4, 5, 4, 1, 2, 1, 1)
print(t.count(1))
print(t.index(5))

# Example 3 : creating a tuple with different types
a = (1, 2, 3, "nepal", 3.4, 6, 9)
print(a)
print(type(a))

