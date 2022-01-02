# we can write to a file using write() and writeline() method
# write() method le file ko content remove garera rewrite garcha


# Example 1 :
myfile = open("hello.txt", "w")
myfile.write("Hello, world! Let's start.\n")
myfile.write('''\t\t\t\tHere i am this is me
                this no where else
                so  near u make a dream
                it's got a new world
                it's got a new start
                it's life with peering on young heart''')
myfile.close()



# Example 2 : creating multipication tables from 2 to 15
for i in range(2, 16):
    with open(f"Multiplication_table_of_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i} X {j} = {i*j}\n")
    f.close()




