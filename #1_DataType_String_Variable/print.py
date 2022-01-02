# Example 0
number = 47

print("This is " + str(number))                 # concatinate garda kheri number type ko data lai string ma laijanai parcha then only we can print
print("This is ", number)                       # comma diyera print garna cha vani number lai string ma lagi rakha pardaina.. we can print both string type of data & number type of data


# Example 1
# For multi line print
print('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')


# Example 2
a = 30
b = 15
print("The sum of a and b is", a + b)


# Example 3
a = 458
b = 15

print("The remainder when a is divided by b is", a%b)

# Example 4

name = "Dhiraj"
age = 24
print("My name is ", name, "And my age is", age)

#next way
name = "Dhiraj"
age = 24
message ="My name is {} and my name is {}".format(name, age)
print(message)