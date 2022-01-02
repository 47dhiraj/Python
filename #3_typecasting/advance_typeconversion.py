# IMPLICIT type conversion (yaha hierarchy ko basis ma type promotion  hunxa i.e integer ko vanda float ko hierachy badi hunxa)

num_int = 123
num_flo = 1.23

print("datatype of num_int:", type(num_int))
print("datatype of num_int:", type(num_flo))

num_new = num_int + num_flo                                                     #yo line ma num_new varibale ma add hune bela implicit type conversion vayera value add hunxa
print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))


# EXPLICIT type conversion  (integer can be converted to float & float can also be converted to integer explicitly)

# Example 1 ==> integer & float
a = 2
b = 4.0
print("Data type of a", type(a))
print("Data type of b", type(b))

converted_a = float(a)                                              # converting integer to float type explicitly
print("Data type of a after converison", type(converted_a))

converted_b = int(b)                                                # converting float to integer type explicitly
print("Data type of b after converison", type(converted_b))


sum = converted_a + converted_b
print("sum", sum)
print("Data type of sum", type(sum))


# Example 2 ==> (integer & string)
# string to integer
d = "47"
print(type(d))

converted_d = int(d)
print(type(converted_d))
print(converted_d)


# integer to string
e = 47
print(type(e))

converted_e = str(e)
print(type(converted_e))
print(converted_e)