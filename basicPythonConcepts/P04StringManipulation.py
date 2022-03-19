varStr1 = "HectorHernandez@heaven.com"
varStr2 = "Endless blessings"
varStr3 = "Hector"
print(varStr1)
print("Character in index 0 is",varStr1[0])   #print H
print("Character in index 15 is",varStr1[15])  #print @
print("SubString or Range from:to-1:",varStr1[6:15])  #print Hernandez
print("concatenation of var1 + var2: ", varStr1 + varStr2)
print("concatenating 2 substring: ", varStr1[6:15] + varStr1[0:6])  #print HernandezHector
#to check if a string is included in another one: use (str3 in str1)
print("check str3 is in str1, return True or False:", varStr3 in varStr1)
print("check if constant heaven.com is in varStr1:", "heaven.comFalse" in varStr1)

# to split the content of a string variable into two base on a specific character. this will
# move the result to a List variable with two elements, and then we can use then with index 0 and 1.
varSplit = varStr1.split("@")
print("the created list is:", varSplit)
print("the name is in index 0:", varSplit[0])
print("the domain name is in index 1:", varSplit[1])

# to trim spaces from a string variable we use the strip string's method,
varStr4 = "   Awesome    "
varStr5 = "  Super Wonderful Amazing    "
print("original:", varStr4)
print("strip method strip/trim all spaces from on left and right of the string:", varStr4.strip())
print("original:", varStr5)
print("strip all spaces from left and right:", varStr5.strip())
print("lstrip, strip/trim all spaces from the left:", varStr4.lstrip())
print("rstrip, strip/trim all spaces from the right:", varStr4.rstrip())

var1 = "abcdefghijk"     # 1: variable with string content to reverse.
print("var1 length: ", len(var1))   # print the number of characters in the variable.
list1 = list(var1)       # 2: Convert the variable to a list of characters
print("list 1:", list1)  # print the new list.
var2 = reversed(var1)   # 3: Reverse var1 into a list of character

reversedVariable = ""   # 4 initialize the variable to have the new reversedVariable.
for item in var2:       # 5 Enter in a loop print and move each character to reversedVariable
    print("reversed var2: ", item)  # print each character
    reversedVariable = reversedVariable + item   # concatenate to for the new reversedvariable

print("reversedVariable:" + reversedVariable)  # print the reversedVariable.

