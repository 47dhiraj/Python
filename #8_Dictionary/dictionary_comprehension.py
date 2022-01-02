'''
Dictionary comprehension is an elegant and concise way to create a new dictionary from an iterable in Python.
Dictionary comprehension consists of an expression pair (key: value) followed by a for statement inside curly braces {}
'''

# Example 1 :
# In simpler but lengthy way:
squares = {}
for x in range(6):
    squares[x] = x * x

print(type(squares))
print(squares)

# using dictionary comprehension way:
squares = {x: x*x for x in range(6)}
print(type(squares))
print(squares)



'''
A dictionary comprehension can optionally contain more for or if statements.
An optional if statement can filter out items to form the new dictionary.
'''
# Example 2 :
# In simpler but lengthy way:
odd_squares = {}
for x in range(11):
    if x % 2 == 1:
        odd_squares[x] = x * x

print(type(odd_squares))
print(odd_squares)

# using dictionary comprehension way:
odd_squares = {x: x*x for x in range(11) if x % 2 == 1}
print(type(odd_squares))
print(odd_squares)














