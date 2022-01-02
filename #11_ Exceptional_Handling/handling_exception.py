# Example 1: Basic Example
try:
    a = 12/0                      # something/0 infinity ho so tei vayera Exception aaucha
except ZeroDivisionError as e:                          # receiving the exception
    print(e, ' Exception occured.')



# Example 2 : try..except..finally
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
    exit()
finally:
    print("We are done")



# Example 3 :   try..except..else
try:
    i = int(input("Enter a number: "))
    c = 1/i
except Exception as e:
    print(e)
else:
    print("Division successfully done")



# Real world exception handling : Handling Exception in Actually
def validate_age(age):
    if age < 18:
        error = ValueError("Age must be greater than 18 to vote. Re enter your age.")  #yo line ko ValueError vaneko user aafaile error generate garna ko lagi python le diyeko inbuilt functio ho
        raise error            #yaha batw error raise vayera siddai exception handling ma jancha
    print("Your age is Valid")       #exception na aaye matra yo statment execute hunxa



age = int(input("Enter your age : "))

try:
    validate_age(age)
except ValueError as e:        #error aaye paxi run hunxa yo
    print(e)

    while(age < 18):
        age = int(input("Enter your age : "))
        print("Age must be greater than 18 to vote. Re enter your age.")

    validate_age(age)
finally:
    print('Finally error solved')