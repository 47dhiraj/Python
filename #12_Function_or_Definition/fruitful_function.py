#if some function return something then those functions are called fruitful functions

# Example 0 :
def percent(marks):
    percent = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
    return percent

total_marks = [45, 78, 86, 77]
print(percent(total_marks))


# Example 1:
def sum(a, b):
    x = a+b
    return x                        #yo line le value return garxa

result = sum(40, 7)                  #return vayeko value result ma halxa
print(result)


# Example 2: Return True of None
def greet(name):
    lname = name.lower()
    if lname == "hitman":
        print("Welcome " + name)
        return True
    return                          # by default return matra lekhyo vani None return huncha

name = input("Enter the name : ")
if greet(name) == None:
    print("Invalid Name")


# Example 3: Return strings
def greet(name):
    lname = name.lower()
    if lname == "hitman":
        return "Hi " + name + " ! Welcome."
    return "Get Lost "

name = input("Enter the name : ")
print(greet(name))





