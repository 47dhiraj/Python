#chaining of various decorators
def first_decorator(func):
    def inner():
        print("Decorating by first decorator")
        func()
    return inner

def second_decorator(func):
    def inner():
        print("Decorating by second decorator")
        func()
    return inner

@first_decorator     #first ma first_decorator call hunxa... jasle second_decorator function lai parameter jasari linxa.......i.e it calls second_decoraotr and second decorator again calls printer() function
@second_decorator     #second_decorator ma chai printer() function argument jasari jani ho....but first_decorator ma chai second_decorator ko inner return vayeko argument jasari jani ho
def printer():
    print("Inside printer function")
printer()



















