import json

with open('source_file.json') as source_file, open('destination_file.json', 'w') as destination_file:      # source_file.json file lai pahila open gareko
    data = json.load(source_file)                                                                          # json file ma vayeko JSON data lai load or read garna load() method ko use garincha
    json.dump(data, destination_file)
    source_file.close()
    destination_file.close()
