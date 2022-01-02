# empty dictionary

# Example 1 ==> using curly braces
my_dict = {}
print(my_dict)
print(type(my_dict))

# Example 2 ==. using dict() method
new_dict = dict()
print(new_dict)
print(type(new_dict))

# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}

# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}

# from sequence having each item as a pair
my_dict = dict([(1, 'apple'), (2, 'ball')])

myDict = {
    "fast": "In a Quick Manner",
    "dhiraj": "A Programmer",
    "marks": [1, 2, 5],
    "anotherdict": {'dhiraj': 'Player'}
}

print(type(myDict))
print(myDict)

# accessing specific value
val = myDict["dhiraj"]
print(val)

# For keys of the dictionary
print(list(myDict.keys()))

# For values of the dictionary
print(myDict.values())

# For (key, value) pair of the dictionary
print(myDict.items())

# For getting the value assosciated with key ==> using .get() & []
# The difference between .get and [] sytax in Dictionaries?

print(myDict.get("dhiraj1"))  # Returns None as dhiraj1 is not present in the dictionary
# print(myDict["dhiraj1"])  # throws an KeyError as dhiraj1 is not present in the dictionary

# For checking if the key exists
if "dhiraj1" in myDict:
    print("Yes, 'dhiraj1' is one of the keys in the myDict dictionary")

# For Updating the dictionary
updateDict = {
    "Hari": "Friend",
    "Rita": "Friend",
    "Gita": "Friend",
    "dhiraj": "A Developer"
}
myDict.update(updateDict)   # Updates the dictionary by adding key-value pairs from updateDict using update() method
print(myDict)


# len() returns the number of pairs
myDict["name"] = "RAM"
print(len(myDict))


# For deleting a pair
del myDict["Hari"]
print(myDict)

# deleting  all items
myDict.clear()
print(myDict)

