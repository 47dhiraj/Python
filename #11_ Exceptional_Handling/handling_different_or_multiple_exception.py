# Handling different exception

# Example 1:
try:
    a = int(input("Enter a number: "))
    c = 1 / a
    print(c)

except ValueError as e:
    print("Please Enter a valid value")

except ZeroDivisionError as e:
    print("Make sure you are not dividing by 0")



# Example 2 :
try:
    i = int(input("Enter a number: "))
    b = 12/i
    print(b)

    a = []
    print(a[1])

except IndexError as ie:                    #yo IndexError chai python inbuilt exception ho
    print(ie)

except ZeroDivisionError as e:              #yo ZeroDivisionError chai python ibuilt exception ho
    print(e)

except Exception as e:
    print("other exceptions :", e)



# Example 3: Catching multiple exceptions in one except
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a/b
    print(c)

    i = []
    result = i[0]
except(IndexError, ArithmeticError):       #yo line le multiple statement catch garxa
    print("Exception Occured")


# Example 4 : using else: block
try:
    a = []
    result = a[0]

except(IndexError, ArithmeticError):
    print("Exception")

else:
    print("No exception")

finally:                    # exception aaye pani na aaye pani finally block run huncha
    print("Clearing Resource")


