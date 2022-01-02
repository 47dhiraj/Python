import csv

movies_list = []
items_list = []
result = []

with open('movies.csv', mode='r') as movies_csv, open('items.csv', mode='r') as item_csv:
    movies = csv.reader(movies_csv, delimiter=',')
    items = csv.reader(item_csv, delimiter=',')

    for row in items:
        items_list.append(row[0])
    print(len(items_list))

    for row in movies:
        movies_list.append(row[0])
    print(len(movies_list))



for i in movies_list:
        if i in items_list:
            result.append(i)
print(len(result))

with open('result.csv', mode='w', newline='') as resultcsv:
    result_csv = csv.writer(resultcsv, delimiter=',')
    for i in result:
        result_csv.writerow([i])



not_matched = []
for i in movies_list:
    if i not in result:
        not_matched.append(i)
print(len(not_matched))

with open('not_matched.csv', mode='w', newline='') as notmatchcsv:
    not_matchcsv = csv.writer(notmatchcsv, delimiter=',')
    for i in not_matched:
        not_matchcsv.writerow([i])

