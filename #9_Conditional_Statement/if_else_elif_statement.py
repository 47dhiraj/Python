# if else logic in Booleans Type
happy = True
if happy:
    print('Smile')



# if else in integer type of data
# Example 1:
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if (num1 > num4):
    f1 = num1
else:
    f1 = num4

if (num2 > num3):
    f2 = num2
else:
    f2 = num3

if (f1 > f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")


# Example 2

sub1 = int(input("Enter first subject marks\n"))
sub2 = int(input("Enter second subject marks\n"))
sub3 = int(input("Enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail because you have less than 33% in one of the subjects")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total percentage less than 40")
else:
    print("Congatulations! You passed the exam")


# Example 3 :
marks = int(input("Enter Your Marks\n"))

if marks >= 90:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Your grade is " + grade)


# if else in string type of data
# Example 1:
me = "Ram"
you = "Shyam"
print("me == you ?", me == you)


# Example 2:
text = input("Enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
else:
    spam = False

if(spam):
    print("This text is spam")
else:
    print("This text is not spam")


# Example 3:
names = ["Ram", "Shyam", "Hari", "Hitman"]
name = input("Enter the name to check\n")

if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")

