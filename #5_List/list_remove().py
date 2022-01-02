# removing the list item using del method
work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(work_days)

# Example 1 : using remove method
work_days.remove("Monday")
print(work_days)

# Example 2: using del method
del work_days[0]
print(work_days)

# Example 3:
backpack = ["pizza slice", "button", "pizza slice", "fishing pole", "pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]
print(backpack)

# Removing first single occurance in the list
backpack.remove("pizza slice")
print(backpack)


# Best way : REMOVING ALL OCCURANCES IN LIST ==> using while loop
while("pizza slice" in backpack):
    backpack.remove("pizza slice")
print(backpack)


# Good way : REMOVING ALL OCCURANCES IN LIST ==> using for loop
for item in backpack[:]:    #uses copy to keep index
    if item == "pizza slice":
        backpack.remove(item)
print(backpack)

# Alternative way : REMOVING ALL OCCURANCES IN LIST ==> using for loop
# for item in backpack:
#    if(item == "pizza slice"):
#        backpack.remove(item)
# print(backpack)

