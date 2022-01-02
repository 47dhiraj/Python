# While Loop needs ==> initialization, stopping condition, and increment.
# Example 1:
i = 1
while i <= 10:
    print("Iteration :" + str(i))
    i += 1



# Example 2:
i = 10
while(i >= 1):
    print('Count Down Iteration :', str(i))
    i -= 1



# Example 3:
initialization = 6
stop_at = 10
increment = 1

while(initialization < stop_at):
    print("Current Value :", initialization)
    initialization += increment


# ELSE WITH WHILE STATEMENT ==> The else statement for a while will execute if no break is hit.
i = 0
while(i < 10):
    print('Iteration :', str(i))
    i += 1
else:
    print("While loop ended & else part ran")




# Break statement in While loop
index = -1
i = 1
while(i <= 20):
    print('Iteration', i)
    if i**2 >= 100:
        index = i
        print('Index :', index)
        break                               # break statement le jun sukai loop vaye pani loop ko iteration process lai nai terminate garaidincha & break statement doesn't care if the looping condition meets or not.
        print('statement below break statement does not executes')
    i += 1

print('Final value of i = ', i)
print('Final value of index =', index)




# Continue Statement in While Loop
index = -1
i = 1

while(i <= 15):
    if i**2 == 100:
        index = i
        print('Condition already met at Iteration = ', i, ' & Index = ', index)
        i += 1
        continue                                    # contine keyword le if or else statement batw bahira niskincha & also current iteration lai terminate garera, loop ko next iteration lai run garaucha
        print('statement below continue statement does not executes')
    print('Iteration :', i)
    i += 1

print('Total number of iteration run = ', i-1)




# Indefinate / Sentinel loops
response = input("Do you want to continue ? Y/N: ")

while response.lower() == "y":
    response = input("Do you want to continue ? Y/N: ")

print('While Loop Terminates')
