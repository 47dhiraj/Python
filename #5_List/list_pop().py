########## REMOVE ELEMENT WITH POP ##########

#The pop method remove the elements & also returns the elements which is being removed

# Example 1:
work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
popped = work_days.pop(1)

print("You remove element : " + popped)
print('Updated list  :', work_days)



# Example 2:
fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.pop(len(fruits)-1)
print(fruits)




