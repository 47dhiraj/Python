# remove() method ==>    removing an element not present in my_set ==> you will get an KeyError
# discard() method ==>   discarding an element not present in my_set ==> you won't get an error

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
my_set.discard(4)
print(my_set)

# discarding an element not present in my_set ==> you won't get an error
my_set.discard(2)
print(my_set)



# remove an element
my_set.remove(6)
print(my_set)

# removing an element not present in my_set ==> you will get an KeyError
# my_set.remove(2)
