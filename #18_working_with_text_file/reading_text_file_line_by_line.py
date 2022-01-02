# lines from a file can be read using readline()  and readlines() method

# readline() method le ek choti ma auta matra line read garcha (i.e file ko purai lines haru read garna lai loop vitra rakhna parcha)
# readlines() le ekkai choti ma file ko sabbai lines lai read garcha (i.e sabai file lai read garna yeslai kunai loop ko jarurat pardaina .. just chittika display garna ko lagi matra loop ko jarurat parne ho)


# Example 1 : using while loop  with readline()
file = open("everest.txt", "r")
while True:
    line = file.readline()                        # file batw single line lai read garcha
    if len(line) == 0:                            # checking if the end of file is reached or not
        break
    print(line)
file.close()



# Example 2 : using while loop with readline()
file = open("everest.txt", "r")
count = 0
while True:
    count += 1
    line = file.readline()                          # Get single line from file
    if not line:                                    # checking if the end of file is reached or not
        break
    print("Line{}: {}".format(count, line.strip()))

file.close()



# Example 3 : using for loops with readlines() method
count = 0
with open("everest.txt") as fp:
    Lines = fp.readlines()
    print(Lines)
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))



# Example 4 : reading file without using read() and readline() method
file = open("everest.txt", "r")
count = 0
for line in file:
    count += 1
    print("Line{}: {}".format(count, line.strip()))

file.close()


# Example 5 : reading file in more advance & easy way
with open('everest.txt') as f:
    for index, line in enumerate(f):
        print("Line {}: {}".format(index, line.strip()))




