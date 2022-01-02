# Various example of Nested Loops


# # Example 1 : Nested For Loop
# for i in range(5):
#     print('i ' + 'j')
#     for j in range(2):
#         print(i, j)
#     print()
#
#
#
# # Example 2 : Nested While Loop
# print("All the sums with output:")
# i = 0
# print("Getting sums up to", 10)
#
# while (i < 11):
#     sum = 0
#     j = i
#     while j > 0:
#         if j > 1:
#             print(j, "+", end=" ")                  # end=" " le print gareko wala line lai next line ma laijanna
#         else:
#             print(j, "=", end=" ")
#         sum += j
#         j -= 1
#     print(sum)
#     i += 1
#
#
#
# # Example 3: Nested While Loop another example
# print("All the sums with output:")
# i = 10
# print("Getting sums up to", i)
# while (i > -1):
#     sum = 0
#     j = i
#     while j > 0:
#         if j > 1:
#             print(j, "+", end=" ")
#         else:
#             print(j, "=", end=" ")
#         sum += j
#         j -= 1
#     print(sum)
#     i -= 1




# Flag of Nepal with numeric digit
i = 0
while (i < 11):
    sum = 0
    j = i
    while j > 0:
        if j > 1:
            print(j, "+", end=" ")                  # end=" " le print gareko wala line lai next line ma laijanna
        else:
            print(j, "=", end=" ")
        sum += j
        j -= 1
    print(sum)
    i += 1

i = 0
while (i < 11):
    sum = 0
    j = i
    while j > 0:
        if j > 1:
            print(j, "+", end=" ")                  # end=" " le print gareko wala line lai next line ma laijanna
        else:
            print(j, "=", end=" ")
        sum += j
        j -= 1
    print(sum)
    i += 1
i = 0
while (i < 3):
    print("||")
    i += 1