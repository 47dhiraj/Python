# Example 1:
A = [{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]

print(len(A))
for i in A:
    print(i)


for i in range(len(A)):
    print(A[i]['name'])


# for finding dictionary values
print(A[i].values())
