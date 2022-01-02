# decorators auta yesto funciton jasle function nai as a argument accept garcha & function nai return garcha
# Just Decorator le kasari kaam garcha vanera basic bujna ko lagi matra ho yo talako code


def make_pretty(func):              #yo make_pretty() function chai khas ma decorator ho ... jasle auta function receive garxa & auta function nai return garcha
    def inner():                    # yo chai decorator function ko inner function ho which is always automatically called .. no need to call
        print('Before Decorating')
        func()                      # ordinary() function lai feri call garcha
        print("After Decorating")
    print(type(inner))
    return inner


def ordinary():
    print("Inside the Ordinary() function")


#using the concept of decorators
pretty = make_pretty(ordinary)       # calling make_preety() decorator by passing function name ordinary    #yaha pretty chai function ho ..jasma function nai return aayera baseko xa
# print(type(pretty))                  # preety ko type check garni ho vani yo function nai ho
pretty()











