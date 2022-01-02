# in & not in operator working with String

# Example 1:
string1 = "My name is Hitman"

if "Hitman" in string1:
    print('you are Hitman')
else:
    print('you are unknown')

# Example 2:
string1 = "My name is Agent"

if "Agent" not in string1:
    print('you are Unknown')
else:
    print('you are Agent 47')



# in & not in operator working with list

# Example 1:
list1 = [46, 47, 48]

if 47 in list1:
    print('you are Hitman')
else:
    print('you are unknown')

# Example 2:
list1 = [46, 47, 48]

if 47 not in list1:
    print('you are not Hitman')
else:
    print('you are Hitman')



# in & not in operator working with tuple

# Example 1:
tuple1 = (46, 47, 48)

if 47 in tuple1:
    print('you are Hitman')
else:
    print('you are unknown')

# Example 2:
tuple1 = (46, 47, 48)

if 47 not in tuple1:
    print('you are not Hitman')
else:
    print('you are Hitman')



# in & not in operator working with dictionary

# Example 1:
dict1 = {46: "Unknown", 47: "Agent 47", 48: "Unknown"}

if 47 in dict1:
    print('you are', dict1[47])
else:
    print('you are unknown')


# Example 2:
dict1 = {46: "Unknown", 47: "Agent 47", 48: "Unknown"}

if 47 not in dict1:
    print('you are Unknown')
else:
    print('you are', dict1[47])