# One function calling another function is called function stacking

# Example 1 :
def test3():
    print("inside of test3 function")

def test2():
    test3()
    print("inside of test2 function")

def test1():
    test2()
    print("inside of test1 function")

test1()
print("after test1 function")



# Example 2 :
def greet(name, be_nice=True):
    if be_nice:
        return "Hi " + name + "! Welcome.."
    return "Go away " + name

def greet_all(people):
    for person in people:
        print(greet(person))

people_to_greet = ["Ram", "Shyam", "Hari"]
greet_all(people_to_greet)
