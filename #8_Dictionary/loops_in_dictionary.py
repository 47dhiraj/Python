# Iterations on Dicionary

# Example 1:
details = {'name': 'Ram', 'age': 24}  # details vanni yeuta dictonary ho. Yesma Key and value huncha "curly bracket" leh vancha yo dictionary ho.
print(details.items())

# For looping through values
for x in details.values():
    print(x)

# For LOOPING THROUGH KEYS
for k in details:  # k is a variable but k by convention for key
    print("key :", k, "&", "value :", details[k])

for key in details.keys():
    print("key :", key, "&", "value :", details[key])

# For LOOPING THROUGH KEY-VALUE PAIRS
for key, val in details.items():
    print(key, val)

# Example 2:
emails = {
    "dhiraj": "dhiraj@email.com",
    "hari": "hari@example.com",
    "ram": "ram@gmail.com"
}

# For looping through values
for x in emails.values():
    print(x)

# For LOOPING THROUGH KEYS
for key in emails.keys():
    print("key :", key, "&", "value :", emails[key])

for k in emails:
    print(k)

for k in emails:
    print("index", k, "is", emails[k])


# For LOOPING THROUGH KEY-VALUE PAIRS
for k, elem in emails.items():
    print(k, elem)
