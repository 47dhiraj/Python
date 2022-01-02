import json

with open('source.json') as f:                  # source.json file lai pahila open gareko
    data = json.load(f)                            # json file ma vayeko JSON data lai load or read garna load() method ko use garincha
    f.close()

# Note : python ko dictionary & JS ko JSON ko data structure exact same nai huncha

print(data)                                     # json data lai print garera hereko
print(type(data))                               # Dictionary ho type cha..

# json data ko particular key lai access garne tarika
print(data["firstName"])
print(data["lastName"])
print(data["gender"])
print(data["age"])
print(data["phoneNumbers"])

# JSON Array lai access garney tarika
print(data["phoneNumbers"][0])

# nested json data lai access garne tarika
print(data["address"]["streetAddress"])
print(data["address"]["city"])
print(data["address"]["state"])
print(data["address"]["postalCode"])


# JSON Array vitra ko json lai access garney tarika
print(data["phoneNumbers"][0]["type"])
print(data["phoneNumbers"][0]["number"])