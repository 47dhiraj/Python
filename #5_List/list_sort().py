# we can sort the list using python built in sort() method

# Example 1:
numbers = [1, 11, 115, 13, 1305, 43]
print(numbers)

numbers.sort()              # Remember ==> if no return, modifies the original list
print(numbers)


# Example 2:
work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
print(work_days)

work_days.sort()            # Remember ==> if no return, modifies the original list
print(work_days)


# Example 3 : returns sorted list without affecting original list
numbers = [1, 11, 115, 13, 1305, 43]
print('Original List Before sorting :', numbers)

numbers_sorted = sorted(numbers)            # here sorted(numbers) returns a new list so original list(i.e numbers) is unaffected!

print('Original List after sorting : ', numbers)
print('Sorted list : ', numbers_sorted)


# Example 4 : Immediately creates the copy for sorted list
numbers = sorted([1, 11, 115, 13, 1305, 43])
print(numbers)


# Example 5 : Sort in the REVERSE Order
numbers = [1, 11, 115, 13, 1305, 43]
print(numbers)

numbers.sort(reverse=True)              # Remember ==> if no return, modifies the original list
print(numbers)

# Alternative way for reverse sorting
numbers = sorted([1, 11, 115, 13, 1305, 43])
numbers.reverse()
print(numbers)

# Alternative way for reverse sorting
numbers = [1, 11, 115, 13, 1305, 43]
print(sorted(numbers, reverse=True))


# CASE SENSITIVE SORT
# Example 6:

#When working with strings, 'a' and 'A' are different.

letters = ['a', 'A', 'B', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']
print(letters)

# print(sorted(letters))                          # by default Capital letters are considered first than lower letters
# print(letters)

# letters = sorted(letters)
# print(letters)

letters = sorted(letters, key=str.lower)      # sorting lower or small letters first
print(letters)


# Sort by length of string
random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "a"]
print(sorted(random, key=len))

# SORT NUMBERS WITH LEXICOGRAPHICAL SORTING

numbers = [1, 54, 76, 12, 111, 4343, 6, 8888, 3, 222, 1, 0, 222, -1, -122, 5, -30]
print(sorted(numbers, key=str))             # sorting numbers similar to strings

'''

Basically, when we are working with strings, 
"111" < "12"  because we compare by character left to right
So we can cast each to a str using the str constructor 

'''

