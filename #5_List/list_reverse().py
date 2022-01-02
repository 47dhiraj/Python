# Reversing the order of the elements in the list

# Example 1: reverse the list using reverse() method
backpack = ["pizza slice", "button", "fishing pole", "nunchicks", "sandwich from mcdonalds"]
print(backpack)

backpack.reverse()
print(backpack)

# Example 2: reverse the list using slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h"]
data[:] = data[::-1]
print(data)

# Example 3: Iterating the list in the reversed way using reversed() method
data = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(data)
data_reversed = []

for item in reversed(data):
    data_reversed.append(item)
print(data_reversed)


# Example 4 ==> SWAP AND REVERSE ALGORITHMS
data = ["a", "b", "c", "d", "e", "f", "g", "h"]

for index in range(len(data) // 2):
    data[index], data[-index-1] = data[-index-1], data[index]

print(data)
