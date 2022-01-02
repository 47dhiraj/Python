import requests

title = input("Enter movie name: ")
year = input("Enter movie year: ")

url = "https://yts.mx/api/v2/list_movies.json?query_term=" + title + " (" + year + ")"
print(url)


response = requests.get(url)
print(response.json())
print(response.json()["status"])
print(response.json()["data"])


