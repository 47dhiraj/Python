# Assertion vannale Right or True cha ki nai vanera chekcing garney ho.. yedi False or wrong huncha vani exception aaucha

# # Example 1 :
# a = int(input("Enter Hitman code : "))
# assert a == 47, "Invalid code Entered."    # a ko value 47 aauxa vanera expect garejastai ho...so 47 xa ki nai vanera check garxa....xaina vane exception aauxa
# print("Valid code Entered.")


# Example 2:
def validate_age(age):
    if age < 18:
        assert age >= 18, "Age must be greater than 18 to vote. Re enter your age."
    print("Your age is Valid")       #exception na aaye matra yo statment execute hunxa



age = float(input("Enter your age : "))
try:
    validate_age(age)
except AssertionError as e:        #error aaye paxi run hunxa yo
    print(e)

    while(age < 18):
        age = float(input("Enter your age : "))
        print("Age must be greater than 18 to vote. Re enter your age.")

    validate_age(age)
finally:
    print('Finally error solved')