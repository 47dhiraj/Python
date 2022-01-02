# Example 1 : Input function for String type of data
a = input("Enter a number: ")
a = int(a)                                                  # Convert a to an Integer(if possible)
print(type(a))


# Example 2: Input for string type of data
b = input("Enter first number: ")
c = input("Enter second number: ")
b = int(b)                          # typeconversion of the data
c = int(c)
avg = (b + c)/2
print("The average of a and b is", avg)


# Example 3:
#Note : input vanni built in function le jahile user batw string format ma data lincha

#Terminal batw input line tarika
name = input("Enter ur Name : ")

age_str = input("Enter ur age : ")          #age_str varibale ma string type ko age basxa i.e "23"
age_int = int(age_str)                      # age lai integer ma typecasting gareko

print("name", name)
print("age", age_int)
