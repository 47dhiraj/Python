# # Example 1: url batw taner variable ma lekhni
#
# import urllib.request
#
# url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
# url_object = urllib.request.urlopen(url)
# data = str(url_object.read())
# url_object.close()
# print(data)


# Example 2 : Extracting data from url and writing to the text file
import urllib.request

url = "https://www.w3.org/TR/PNG/iso_8859-1.txt"
destination_filename = "url_data.txt"          #automatic file gernerate garxa pahila
urllib.request.urlretrieve(url, destination_filename)    #url ma vayeko kura destination file ma lekhxa
