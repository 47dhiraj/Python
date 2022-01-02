# Raising error by user themselves & handling these errors in exception

def validate_age(age):
    if age < 18:
        error = ValueError("Age must be greater than 18 to vote. Re enter your age.")  #yo line ko ValueError vaneko user aafaile error generate garna ko lagi python le diyeko inbuilt functio ho
        raise error            #yaha batw error raise vayera siddai exception handling ma jancha
    print("Your age is Valid")       #exception na aaye matra yo statment execute hunxa



age = int(input("Enter your age : "))

try:
    validate_age(age)
except ValueError as e:        #error aaye paxi run hunxa yo
    print(e)

    while(age < 18):
        age = int(input("Enter your age : "))
        print("Age must be greater than 18 to vote. Re enter your age.")

    validate_age(age)
finally:
    print('Finally error solved')





















