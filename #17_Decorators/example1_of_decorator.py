# Example 1 :

def make_pretty(func):              # make_preety decorator receiving ordinary() function as argument
    def inner():
        print('Before Decorating')
        func()                      # yo func() call hunu vaneko ordinary() function call hunu & execute hunu ho
        print("After Decorating")
    return inner                    # returning the inner function of decorator

@make_pretty                        # decorating the ordinary() function by make_pretty() decorator function  # yo ordinary() function lai make_pretty() function ma a argument lagera halcha
def ordinary():
    print("Inside Ordinary Function")

ordinary()                          # yo line execute vaye pachhi sidai line 10 ko @make_pretty ma hit huncha & siddai make_pretty() decorator execute huncha # yo ordinary() function, siddai make_pretty() vanni decorator function ma as argument jancha



