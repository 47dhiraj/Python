# Example 1 : Break statement in While loop
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


# Example 2 : Break statement in For Loop
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C++":
        print(language + " found inside if block")
        break
        print("This line never executes")
    print(language + ": is not the language what we are looking for.")



# Example 3 : Break Statement in inner For Loop
# yedi sabbai breaking condition run garauna cha vani yesasri garni
for x in range(10):
    for y in range(10):
        if x*y > 50:
            print(x, ' * ', y, '=', x*y)
            break                   # yo break statement le inner for loop lai break garcha
        else:
            continue                    # continue statement only executes if the inner for loop doesn't break



# Example 4: Break statement in nested loops(both inner and outer for loop)
# Yedi only first break condition matra run garauna cha vani yesari garni
for x in range(10):
    for y in range(10):
        if x*y > 50:
            print(x, ' * ', y, '=', x*y)
            break                       # yo break statement le inner for loop lai break garcha
    else:                           # for loop vitra ko if run vayena vani matra yo else part run huncha
        continue                    # continue statement only executes if the inner for loop doesn't break
    break                               # yedi else part ko continue run vayena vani matra yo break statement run huncha jasle outer loop lai pani break garcha



