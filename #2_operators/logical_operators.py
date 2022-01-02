# logical operation (i.e True False ko operation)
a = (False and (False or True and True))
print(a)

b = (False and True or True)
print(b)

print('Now applying bitwise operation')
print(a | b)
print(a & b)

# Another Example of Logical operations
bool1 = True
bool2 = False

print("The value of bool1 and bool2 is", (bool1 and bool2))
print("The value of bool1 or bool2 is", (bool1 or bool2))
print("The value of not bool2 is", (not bool2))