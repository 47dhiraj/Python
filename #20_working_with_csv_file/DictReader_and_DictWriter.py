import csv

movies_list = []
items_list = []
result = []

with open('dict_movies.csv', mode='r') as movies_csv, open('dict_items.csv', mode='r') as item_csv:
    movies = csv.DictReader(movies_csv, delimiter=',')
    items = csv.DictReader(item_csv, delimiter=',')

    for row in items:
        items_list.append(row["title"])
    print(len(items_list))

    for row in movies:
        movies_list.append(row["title"])
    print(len(movies_list))



for i in movies_list:
        if i in items_list:
            result.append(i)
print(len(result))

with open('dict_result.csv', mode='w', newline='') as resultcsv:
    fieldnames = ['title']
    result_csv = csv.DictWriter(resultcsv, delimiter=',', fieldnames=fieldnames)
    result_csv.writeheader()
    for i in result:
        result_csv.writerow({'title': i})




not_matched = []
for i in movies_list:
    if i not in result:
        not_matched.append(i)
print(len(not_matched))

with open('dict_not_matched.csv', mode='w', newline='') as notmatchcsv:
    fieldnames = ['title']
    not_matchcsv = csv.DictWriter(notmatchcsv, delimiter=',', fieldnames=fieldnames)
    not_matchcsv.writeheader()
    for i in not_matched:
        not_matchcsv.writerow({'title': i})

