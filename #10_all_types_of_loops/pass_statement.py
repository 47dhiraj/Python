# pass statement in while loop
# Example 1:
response = input("Do you want to continue ? Y/N: ")

while response.lower() == "y":
    response = input("Do you want to continue ? Y/N: ")
else:
    pass

print('Out of while & else statement')



# Example 2: pass statement in simple for range
for x in range(10):
    pass



