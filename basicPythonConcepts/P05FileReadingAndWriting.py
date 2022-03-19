# in this program we will cover the ways to read and write to *.txt file
# to test we have created the hectorTest.txt file in the project root directory:
# C:\\Users\\ssshh\\PycharmProjects\\HectorFirstpythonProject\\hectorTest.txt

# open the file and assign to a variable colorsFile:
# A very important note: always close the file at the end colorsFile.close()
colorsFile = open('..\\hectorTest.txt')

# A file is opened either to read from it or to write to it.
# colorsFile.read()  # To read ALL the content of the file as a whole
# print(colorsFile.read())

# To read the "n" first position of a file use colorsFile.read(n)
# if "n" is not provided by default will read the whole file.
# print(colorsFile.read(13))  # print "Red Green blu" (the carry return is counted)

# note: not recommended to combine .read() and .readline() in a program, because
# the result could be unpredictable, this is why of the comments in before .read..
# also, after using .read() whole file is read and any other .readline() will give empty line.
# to read a file one line at a time user colorsFile.readline()
# print(colorsFile.readline())  # read the whole line.
# print(colorsFile.readline())  # read the whole line.
# print(colorsFile.readline(3)) # read the first 3 characters of the line.

# to read the whole file, one line at at time, using .readline() method without repetition,
# we have to use a logic, and for this we have two choices:
# choice #1:
# currentLine = colorsFile.readline()
# while currentLine != "":
#     print(currentLine)
#     currentLine = colorsFile.readline()

# choice #2:
# using the .readlines() method will read the whole file and move it to a list
# and from the list we can use the power of all the List methods:
# for currLine in colorsFile.readlines():
#     print(currLine)
# Another way:
allLines = colorsFile.readlines()
for readLine in allLines:
    print(readLine)

colorsFile.close()  # closing the file.

# There is a way to open a file and closing it automatically when the program
# finishes, with needing the .close() method, and this is with the "with command"
#      with open('filename.txt','r/w') as objectNameFile

# below code is for writing to the file, we will follow below steps:
# 1- Read the file and store all its lines in a List variable.
# 2- Reverse the List variable.
# 3- Write the reversed List variable back to the file.

with open('../hectorTest02.txt', 'r') as inputFile:  # 'r' for reading the file
    HectorlistOfRecords = inputFile.readlines()   # reads all the lines to a List
    with open('../hectorTest02.txt', 'w') as outputFile:  # 'w' for writing to the file
        for lineRecord in reversed(HectorlistOfRecords):  # reversed function on the List
            outputFile.write(lineRecord)
            print("line: ", lineRecord)
