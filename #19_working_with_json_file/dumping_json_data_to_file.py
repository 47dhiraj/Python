import json

data = {
            "firstName": "Lakhan",
            "lastName": "Chaudhary",
            "gender": "male",
            "age": 25,
            "address": {
                            "streetAddress": "Lakhan chowk",
                            "city": "Lakhaniya",
                            "state": "Lumbini",
                            "postalCode": "12345"
                        },
            "phoneNumbers": [
                                {"type": "personal", "number": "9840000000"}
                            ]
        }

print(type(data))

with open('destination.json', 'w') as f:                # destination.json vanni json file ma dump(write) garna lageko mathiko dictionary
    json.dump(data, f)                                  # dictionary write garna lai dump() method ko use garincha
    f.close()
