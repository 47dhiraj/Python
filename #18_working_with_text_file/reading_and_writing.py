
# # Example 1 : reading from one file and writing to another file
with open("file1.txt") as f:
    content = f.read()

with open("file2.txt", 'w') as f:
    f.write(content)


# # Example 2 : Reading from old file and writing to the new file and finally deleting the old file
import os
oldname = "file1.txt"
newname = "newfile1.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)
