# String compare in Python with input

# Example 1
str_x = 'Hello & Welcome'
str_y = 'hello & Welcome'

if str_x == str_y:
    print("First and second strings are same!")
else:
    print("You entered different strings!")




# Example 2
str_input1 = input("Enter First String? ")
str_input2 = input("Enter Second String? ")

# comparing by ==

if str_input1 == str_input2:
    print("First and second strings are same!")
else:
    print("You entered different strings!")



# Example 3
string_input1 = input("Enter First String? ")
string_input2 = input("Enter Second String? ")


# comparing by != (not equal to)
if string_input1 != string_input2:
    print("Both Strings are different!")
else:
    print("You entered same strings!")


# Example 4
s1 = 'Apple'
s2 = 'Apple'
s3 = 'apple'

# case sensitive equals check
if s1 == s2:
    print('s1 and s2 are equal.')

if s1 == s3:
    print('s1 and s2 are equal.')
else:
    print('s1 and s3 are different.')


# case sensitive equals check
if s1.__eq__(s2):
    print('s1 and s2 are equal.')

if s1.__eq__(s3):
    print('s1 and s3 are equal.')
else:
    print('s1 ans s3 are different')