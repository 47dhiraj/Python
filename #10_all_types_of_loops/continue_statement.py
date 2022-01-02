# Example 1 : Continue Statement in While Loop
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



# Example 2 : Continue Statement in For Loop
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C#":
        print(language + " found")
        continue
        print('This line never executes')
    print(language + ": is not the language what we are looking for.")



# Example 3 : yedi kunai condition meet vaye pani continue garna cha vani yesari garna sakincha
for x in range(10):
    for y in range(10):
        if x*y > 50:
            print(x, ' * ', y, '=', x*y)
            continue


