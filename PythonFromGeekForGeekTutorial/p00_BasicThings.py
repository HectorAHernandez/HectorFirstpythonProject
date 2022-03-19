# using Module: Python has a very rich module library which has serveral functions to to math tasks. to import
# a particular module into our Python program we have to use the 'import' keyword, example:
import math


# functions are piece of code to do a particular task in the whole Python script:
#        format def  function_name(arguments)
def hello():
    print("hello")
    print("hello again")


hello()

# calling the hello() another time:
hello()


# Another function or method:
def get_integer():
    result = int(input("Enter Integer: "))
    return result


# A program start execution from a main() function
def main():
    print("Started execution")
    output = get_integer()
    print("The integer entered is: ", output)

    num = -85
    # fabs is a function in the math module, to get the absolute value of a decimal
    num = math.fabs(num)
    print("absolute value: ", num)


# Now we are required to tell Python of the existence of a Main() function in the program:
if __name__ == "__main__":
    main()

# using for ... loop:
for step in range(5):
    print("step: ", step)
