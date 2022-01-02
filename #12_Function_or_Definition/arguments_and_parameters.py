# Example 0 :
def percent(marks):
    percent = ((marks[0] + marks[1] + marks[2] + marks[3]) / 400) * 100
    return percent

total_marks = [45, 78, 86, 77]
print(percent(total_marks))



# Example 1: Default Parameters
def greet(name="hitman"):             # function definition ma value lai access garney variable lai parameter vanincha
    if name == "hitman":
        return "Hi " + name + " ! Welcome."

print(greet())                        # function call garda value pathayo vani arguments vanincha



# Example 2: Multiple Arguments & Parameters
def greet(name="Unknown", agent=False):
    if name == "hitman" and agent:
        return "Hi " + name + " ! Welcome."
    return "Get Lost " + name

name = input("Enter the name : ")
print(greet(name.lower(), True))



# Example 3 : Positional or Keyword arguments
def greet(name="Unknown", agent=False):
    if name == "hitman" and agent:
        return "Hi " + name + " ! Welcome."
    return "Get Lost " + name

# print(greet("hitman", True))                # Positional Arguments must be in the order of Parameter in function definition
print(greet(agent=True, name="hitman"))        # Keywrod arguments haru function definition ma vayeko paramerters kai ordering ma lekhna parcha vanni hudaina



# Example 4: Detail understanding or Positional or Keyword Arguments
# Anything before the / must be positional-only arguments
# after * all the elements need to be keyword-only arguments
def do_nothing(pos1, pos2, pos3, /, either1, either2, *, keyword1, keyword2, keyword3):
    print("pos1", pos1)
    print("pos2", pos2)
    print("pos3", pos3)
    print("either1", either1)
    print("either2", either2)
    print("keyword1", keyword1)
    print("keyword2", keyword2)
    print("keyword3", keyword3)

do_nothing(1, 2, 3, 4, either2=5, keyword3=6, keyword1=7, keyword2=8)



# Example 5 : Unlimited Arguments or Packing the arguments
def greet_all(*people):
    for person in people:
        print("Hello " + person)

greet_all("Ram", "Shyam", "Hari")


# Example 6 : Unpacking of the Arguments
def print_info(name, age, email):
    print(name + " is " + str(age) + ". Reached at " + email)

info = ["Ram", 25, "ram@email.com"]
print_info(*info)
