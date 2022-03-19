# Method is a piece of code that is intended to perform a particular task in a Python program. A function that
# belong to a class is called a Method.
# All methods/class's functions require the 'self' parameter. 'self' is like the 'this' keyword in others OOP language,
# to make reference to the class variables/attributes.
# to create a new method we use the 'def' keyword:

class Vector2D:    # in a class we define the attributes/class level variable that we want to share with the other
    # classes inheriting this class o method using this class by instantiating this class.
    x = 0.0
    y = 0.0

    # Creating a method named 'set_variables' to set the class attributes x and y. the methods can be used to perform
    # operations on the attributes/class variables/update the attributes:
    def set_variables(self, row1, col1):
        self.x = row1
        self.y = col1


def main():
    # define/create/instantiate vec_01 as an object of the Vector2D class, we can use the created object to use the methods and
    # attributes/class variables defined in the class:
    vec_01 = Vector2D()

    # using the method set_variable() by using the (.) operator to move values to the class attributes/class variables
    vec_01.set_variables(1.2, 2.0)

    # to print the new values in the class attributes/class variables:
    print("X: " + str(vec_01.x) + " Y: " + str(vec_01.y))


# letting the python script/program knows that there is a main() method:
if __name__ == "__main__":
    main()
