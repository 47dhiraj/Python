# Syntax:

# Syntax ==> enumerate(iterable, start_index)

# Example 1:
list = [10, 50, 75, 83, 98, 84, 32]

for x, res in enumerate(list):
    print(x, ":", res)

for x, res in enumerate(list, 0):
    print(x, ":", res)