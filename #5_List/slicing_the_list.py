########## REMOVE ELEMENT FROM LIST USING DEL AND SLICE ##########

work_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# remove first 2
del work_days[0:2]
print(work_days)


# remove last 2 element (start 2 from right and go to end)
del work_days[-2:]
print(work_days)