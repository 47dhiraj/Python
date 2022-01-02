'''


a=b=c=47
e,f,g=4,5,6
print (a)
print (b)
print (c)
print (e)
print (f)
print (g)



name = "Dhiraj Kafle"
# a = 'Dhiraj'
b = 345
c = 45.32
d = True
# d = None

# Printing the variables
print(name)
print(a)
print(b)
print(c)
print(d)

# Printing the type of variables
print(type(name))
print(type(a))
print(type(b))
print(type(c))
print(type(d))


'''



# Global variable and local varibale in python

y = 20                  # global variable is generally declared outside function

def print_number():
  x=10                  # x is local variable because it is declared inside function
  print("The first number is:",x)

print_number()
print("Y is global variable & it's value is :",y)



# we can also declare variable inside function and make it global variable
x = 2
print(x)

def foo():
    global x                        # function vitra ko variable lai global banauna ko lagi global keyword ko use garincha
    x += 3
    y = 4
    z = x * y
    print(z)
    print(x)
    print(y)

foo()

print(x)