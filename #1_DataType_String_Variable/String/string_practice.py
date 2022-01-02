# Practice 1
name = input("Enter your name\n")
print("Good Afternoon, " + name)



# Practice 2
letter = '''Dear <|NAME|>,
Greetings from Django Community. I am happy to tell you about your selection
You are selected! Congratulation !
Have a great day ahead!
Thanks and regards,
Hitman Company
Date: <|DATE|>
'''
full_name = input("Enter Your Full Name\n")
date = input("Enter Full Date\n")
letter = letter.replace("<|NAME|>", full_name)
letter = letter.replace("<|DATE|>", date)
print(letter)




# Practice 3
st = "This is a string with double  spaces"

doubleSpaces = st.find("  ")                    # double space ko index positioning dincha
print(doubleSpaces)



# practice 4
stre = "This is a string with double  spaces  ok"

stre = stre.replace("  ", " ")
print(stre)




# Practice 5
formatted_letter = "Dear Harry,\n\tThis Python course is nice!\nThanks!"
print(formatted_letter)

