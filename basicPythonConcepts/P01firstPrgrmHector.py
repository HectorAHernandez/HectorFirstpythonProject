print("hello Hector")
a = 25.00
print(a)
price, amount, unit = 100.25, 2, "dozen"
print("amount: " + str(amount) + " price: "+str(price) + " unit: "+unit)

variable = "{} {}".format("Economically Free: ", unit)
print(variable)
print("Was, is and will be {} for ever {} ".format("Economically super Free: ", price))
#Using named indexes in the placeholder {}:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#Using numbered indexes in the placeholder {}:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders {}:
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.
#Use "<" to left-align the value:
txt = "We have {:<8} chickens."
print(txt.format(49))

#Use ">" to right-align the value:
txt = "We have {:>8} chickens."
print(txt.format(49))

#use "^" to center-align the value:
txt = "We have {:^8} chickens."
print(txt.format(49))

#Use "=" to place the plus/minus sign at the left most position:
txt = "The temperature is {:=8} degrees celsius."
print(txt.format(-5))

#Use "+" to always indicate if the number is positive or negative:
txt = "Use \"+\" : The temperature is between {:+} and {:+} degrees celsius."
print(txt.format(-3, 7))

#Use -  to always indicate if the number is negative (positive numbers are displayed without any sign):
txt = "Use \"-\" : The temperature is between {:-} and {:-} degrees celsius."
print(txt.format(-3, 7))

#Use " " (a space) to insert a space before positive numbers and a minus sign before negative numbers:
txt = "Use \" \" : The temperature is between {: } and {: } degrees celsius."
print(txt.format(-3, 7))

#Use "," to add a comma as a thousand separator:
txt = "Use \",\" : The universe is {:,} years old."
print(txt.format(13800000000))

#Use "_" to add a underscore character as a thousand separator:
txt = "The universe is {:_} years old."
print(txt.format(13800000000))

#Use "b" to convert the number into binary format:
txt = "The binary version of {0} is {0:b}"
print(txt.format(5))

#Use "c" to Converts the value into the corresponding unicode character:
txt = "The binary version of {0} is {0:c}"
print(txt.format(15))

#Use "d" to convert a number, in this case a binary number, into decimal number format:
txt = "We have {:d} chickens."
print(txt.format(0b101))

# **** For more format conversion look at website: https://www.w3schools.com/python/ref_string_format.asp
txt = "**** For more format conversion look at website: https://www.w3schools.com/python/ref_string_format.asp"
print(txt)

#Python Numeeric Data Type:
    # Create a variable with integer value:
a = 100
print("The type of variable having value", a, " is ", type(a))
# Create a variable with float value:
b = 10.5485
print("The type of variable having value", b, " is ", type(b))
# Create a variable with complex value:
c = 100+3j
print("The type of variable having value", c, " is ", type(c))

#Python "String" data type:
a = "String in a double quote"
b = 'String in a single quote'
# Using ',' to concatenate the two or several strings:
print(a," concatenated using \',\' " ,b)
print(a + " concatenated using \"+\" " +b)

# Python "List" Data Type:
# The List data type is a versatile data type exclusive in Python. In a sense, it is the
# same as in c/c++. But it can simultaneously hold different types of data. Formally a LIST
# in Python is an ordered sequence (based on an index of creation) of some data (allowing multiple data type) written
# using square bracket ([]), and commas (,):
# A list of having only integers
a = [1,2,3,4,5,6]
print("List of Integers: ",a)
# List of having only strings
b = ["Hello","Hector", "King","God"]
print("List of Strings: ",b)
# List of having both integers and strings:
c = ["hello", "Hector", 1,2,3, "Last word", "new last element"]
print("A List with both integers and strings: ", c)
# in a List the index are 0 based. and they can be printed like
print("Elements in the list, 0: ",c[0])
print("Element b2, b3, b1: ",b[2],b[-1],b[1] )
print("The last element in the list is always in c[-1]: ", c[-1])
print("using an index range (from:(to -1) where to is excluded: c[1:6]: {} ".format(c[1:6]))
print(" converting to string {}".format(c[1:5]))
# inserting an element in a list on an specific index position:
b.insert(2,"HERNANDEZ")
print("List b now with HERNANDEZ inserted as 3rd element: ",b)
# Appending to the list
b.append("End List")
print("List b with appended element \"End List\"",b)
# to update or replace the value in an specific index we just need to
# assign a new value.
print(" ** before update the index 2: ", b )
b[2] = "AMPARO"
print(" ** After  update the index 2: ", b )
# to delete the value in an specific index use the del command:
del b[2]
print(" ** After  DELETE the index 2: ", b )


# Python Tuple Data type:
# The tuple is another data type which is a sequence of data similar
# to a list. But it is immutable. That means data in a tuple is
# write-protected. Data in a tuple is written using parenthesis and
# commas.
# All above List retrieve operations can be execute with Tuple, but the ones
# that change the content of the tuple.

#tuple having only integer type of data.
a = (1,2,3,4)
print('A tuple having only integers: ', a)
# A tuple having multiple type of data:
b = ('hello', 1,2,583, "go go king")
print("A tuple with multiple data type ", b)
# index of elements in a tuple are also 0 based:
# to print the fifth element
print("fourth element is b[3]: ",b[3])
print('last element in the tuple is b[-1]: ',b[-1])

# Python Dictionary:
# dictionary in Python is an unordered sequence (no index constructed)
# of key-value pairs. It is similar to the hash table type in other languages.
# Python Dictionaries are written within curly braces in the form of
# key : value. It can contains multiple data type in key and the value part
# simultaneously (integers, string...). Dictionaries are very useful to
# retrieve data in an optimized way among a large amount of data.

# For example of dictionary variable data type:
a = {1: "first name", 2:"last name", "age": 33}
print("value with key=1: ", a[1])
print('value with key=2: ' + a[2])
print("value with key=\"age\": ",a["age"])

# Defining an empty dictionary variable to hold employee data
EmployeeDict = {}
# Now adding key:value pairs to the EmployeeDict:
EmployeeDict["firstName"] = "Hector"
EmployeeDict["lastName"] = "Hernandez"
EmployeeDict["gender"] = "Male"
# Print the whole dictionary
print("EmployeeDict: ", EmployeeDict)
# print only the value of one key:
print("The value of key \"firstName\" is ", EmployeeDict["firstName"])
# modifying the value of a previous key:
EmployeeDict["lastName"] = "Amparo"
print("the new value of the key \"lastName\" is ", EmployeeDict["lastName"])

# Using if condition:
greeting = "Good Morning"
if greeting == "Morning":
    print("1- Condition Matches")
else:
    print("1- Condition does not match")
print("2- Next line after the if")
#Another use of if
temperature = 65
if temperature < 32:
    print("The weather is cold")
elif temperature < 60:
    print("The weather is cool")
elif temperature < 75:
    print("the weather is perfect")
else:
    print("the weather is hot")
print("Next code line")

# for loop:
# for loop has the format for ELEMENT in LIST. It will iterate the list
# and will make the each ELEMENT available for processing:
# define a colors list
print("**** for loop Results ***")
colors = ["red", "green", "blue", "yellow", "white", "black", "pink"]
for color in colors:
    print(color)    #end of for loop
# using Employee list
Employee2List = ["john","Peter","carlos"]
for empl in Employee2List:
    print(empl)  #end of for loop
anyList = [3, 4, 6, 7, 8]
for item in anyList:
    print(item)
# print the list item time 2:
for member in anyList:
    print("member * 2 = ", member*2)
# using the range function for iteration. note the range works like this:
# range(i,j) --> from i to j-1. i.e. range(2,10) goes from 2 to 9.
for number in range(2,10):
    print(number)
# To print the summary of all the numbers in the range:
total = 0
for num in range(2,6):
    total = total + num
    print("number = ", num) #print in each iteration
print("Total of range: ", total)  # print when exit the loop.
# the range function is similar to the for (int j=0; j < size; j++) in java
# or (initial value; condition; increment), so the range format is:
#   range(initial value; condiion j < size; increment).
for j in range(1,10,2):
    print("j = ", j)
# if increment is ommitted, the default is 1.
for x in range(1,5):
    print("x =", x)
# if the intial value is ommitted, the default is zero.
for k in range(3):  # only having the condition --> k=0;k<3;k++
    print("k =", k)
 # the condition is always size - 1 (if index start on 0)
 # using range with a list:
print("using range with a priceList:")
priceList = [10.25, 15.02, 45.00, 5.25]
for i in range(0,len(priceList),1):
    print("price(",i,") =", priceList[i])
# the same as above but with less code
for j in range(len(priceList)):
    print("price-j(",j,") =", priceList[j])
# another way to create the loop without range
for price in priceList:
    print(" price = ", price)

# while loop statement the code is executed as long the condition is true
itr = 4
while itr > 1:
    print("itr: ",itr)
    itr = itr - 1
itr = 6
while itr > 1:
    if itr != 3:
        print("itr2: ", itr)
    itr = itr - 1
# using the "break" keyword inside the loop to exit the while loop
itr = 5
while itr > 1:
    if itr == 3:
        break
    print("itr3: ", itr)
    itr = itr - 1
# using "continue" keyword to SKIP the current iteration of the while
# loop and go to the next iteration
itr = 10
while itr > 1:
    if itr == 8:
        itr = itr - 1
        continue
    if itr == 3:
        break
    print("itr4: ", itr)
    itr = itr - 1

card_number = "*********1234"
print("Card last four characters: ", card_number[-4:])

