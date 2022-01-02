# # Example 1 :
# f = open("text.txt", "r")                    # suru ma file lai read mode i.e "r" ma kholna parcha
# content = f.read()                          # read() vanni python ko inbuilt function le .txt file lai read garni
# f.close()                                   # read gari sake pachi file lai close garni
# print(content)                              # j j read gareko thyo tes content lai print garni



# # Example 2 : Reading by handling the exceptions
# try:
#     f = open("text.txt", 'r')
#     print(f.read())
# except IOError as e:
#     print("IO Error")
#     print(e)



# # Example 3 : Using with open to open file
# with open('paragraph.txt', 'r') as f:
#     a = f.read()
#     print(a)



# # Example 4 : Reading each line of paragraph line by line
# with open('paragraph.txt', 'r') as file:
#     data = file.read().replace('.', '\n')
#     print(data)


# # Example 5 : Reading first some characters of file
# file = open("paragraph.txt", "r")
# print(file.read(10))       #file ko jamma 4 ota charachter read garxa
# file.close()


# # Example 6 : Checking if the word is in the file or not
# f = open('paragraph.txt')
# t = f.read()
# if 'sentences' in t:
#     print("sentences is present in the text file")
# else:
#     print("sentences is not present in the text file")
# f.close()


# # Example 7 : changing the Case of the words in the file
# with open("text.txt") as f:
#     content = f.read()
#     print(content, "\n")
#
#
# if 'FAIL' in content:
#     content = content.lower()
#     print(content)
# else:
#     print("Word is already in lower case")


# # Example 8 :
# file1 = "file1.txt"
# file2 = "file2.txt"
#
# with open(file1) as f:
#     f1 = f.read()
#
# with open(file2) as f:
#     f2 = f.read()
#
# if f1 == f2:
#     print("Content in the file are similar.")
# else:
#     print("Content in the file are not similar")
