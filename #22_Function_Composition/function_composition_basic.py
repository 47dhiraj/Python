# function composition chai thuprai function ko help batw calculate garera ekkai choti output nikalna use huncha

# Example 1:
def compose(f, g):                  # f & g vannale duita function ho (i.e add & multiply)
    return lambda x: f(g(x))        # suru ma number lai multiplication garcha ani addition

def add(x):
    return x+10

def multiply(x):
    return x*2

new_func = compose(add, multiply)
print(new_func(2))



# Example 2 :
def compose(h, f, g):               # h, f & g vannale 3 ta function ho (i.e sub, multiply & add)
    return lambda x: h(f(g(x)))     # suru ma number lai subtraction garcha ani multiplication and finally addition

def sub(x):
    return x-1

def add(x):
    return x+1

def multiply(x):
    return x*2

new_func = compose(add, multiply, sub)
print(new_func(2))