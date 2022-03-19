def another_function():
    print("Another function")


# classes are created by the keyword class
# Attributes are variable to belong to the class level. class variables are always public and can be accessed
# using the (.) operator from the className: MyClass.myattribute
class MyClase:
    # assign the values to the MyClass attributes:
    number = 125
    name = "no-name"


def Main():
    # creating an object of the class MyClass
    my_object = MyClase()

    # Accessing the attributes of the MyClass using teh (.) operator
    my_object.number = 1337
    my_object.name = "Hector"
    print("the name is: " + my_object.name + " and number is: " + str(my_object.number))

# telling Python that there is a main() method in this script:
if __name__ == "__main__":
    Main()

another_function()