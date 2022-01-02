# For range loops

# Basic Understanding of For in range()
initialization = 1                  # yedi initialization value diyena vani by default chai 0 position batw start huncha
stop_at = 11
increment = 1

for i in range(initialization, stop_at, increment):
    print("Iteration :", i)


# Example 1 : Basic Example ==> Default Range starts from 0 & stops at given position
for i in range(11):                     # i ko value 0 batw start huncha by default & stops at 10 (i.e range method vitra auta matra numeric digit cha vani tyo digit vaneko stopping condition ho)
    print("Iteration :", i)



# Example 2: Providing range starting position
for i in range(1, 11):
    print("Iteration :", i)



# Example 3: Providing range step (yedi range() method vitra 3 ta integer cha vani last ko integer vaneko range step ho)
for i in range(0, 9, 2):
    print("Iteration :", i)



# Count down or negative iteration
for i in range(8, 0, -2):
    print("Iteration :", i)


# SUM of numbers using range() method
print(sum(range(1, 4)))


# Creating list with range() method
numbers = list(range(1, 11))
print(numbers)


# For loop range() with list
languages = ["Python", "C++", "Java", "Perl", "C#"]

for i in range(len(languages)):
    print(i, languages[i])



