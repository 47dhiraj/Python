# Syntax of Lambda Function in Python
#  ===> lambda arguments: expression                i.e expression vannale function definition jastai ho
# Lambda function does not include a “return” statement

# # Example 1 :
doubling = lambda x: x * 2
print(doubling(10))
print(type(doubling(10)))


# Alternative or normal function code for Example 1:
def doubling(x):
   return x * 2
print(doubling(10))



# Example 2 : squaring lambda function
square = lambda n: n * n
num = square(5)
print(num)


# Example 3 : Substraction function
sub = lambda x, y: x-y
print(sub(5, 3))












