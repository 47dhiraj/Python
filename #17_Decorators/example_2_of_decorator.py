# Example 2 : Decorating the function having parameter

def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("You cannot divide any number by 0. ZeroDivisionError: division by zero")
            return None
        return func(a, b)                   # divide() function lai call garera aayeko output return huncha
    return inner                            # mathi inner function batw either None return huncha or output retun huncha, so finally tyo kura inner() function batw retun vai rako huncha


@smart_divide                               # decorating divide() function by @smart_divide() decorator function
def divide(a, b):
    return a / b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = divide(a, b)      #yo line execute vaye paxi...line 12 hit hunxa...ani siddai smart_divide() decorator function execute huncha

if result != None:
    print(result)


