
#first approach of finding key from value

a = {"name": "test", "age": 34}

for key, val in a.items():  # .items() vanni inbuilt function ho jasle items haru ko key ra value lincha
    if val == 34:
        print(val, key)



#second approach of finding key from value

b = {"name": "test", "age": 34}
print(b)
print(b['age'])


inverse_dict = dict((value, key) for key, value in b.items())   # dictionary comprehension ko syntax use gareko cha
print(inverse_dict)
print(inverse_dict[34])
