# simple for loop statement
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    print(language)


# For loop in list with break statement
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C++":
        print(language + " found inside if block")
        break
        print("This line never executes")
    print(language + ": is not the language what we are looking for.")



# For loop in list with continue statement
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C#":
        print(language + " found")
        continue
        print('This line never executes')
    print(language + ": is not the language what we are looking for.")


# else instead of continue.. above looping logic can be obtained using else
languages = ["Python", "C++", "Java", "Perl", "C#"]
print("Searching for Perl:")

for language in languages:
    if language == "C#":
        print(language + " found")
    else:
        print(language + " is not the language what we are looking for.")


