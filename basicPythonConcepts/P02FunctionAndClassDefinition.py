# functions are defined using the "def" keyword. Python require 2 empty lines
# between the function definition and other code.

def greet_hector():
    print("Hello Hector... You are the luckiest man on earth!!!")


def greet_any_person(parm_name):
    print("Hello", parm_name)


def add_integers(a, b):
    print("Result: ", a+b)


# using return
def add_int_return(a, b):
    return a+b


# In Python, class are user defined blueprint or prototype of code and variables
# code: function(def..)/ Method:


class HectorCalculator:
    acc_balance = 1250000000000  # this is a class/global variable, this value is
    # available for all instance/objects of the class
    # instance variable are the one created inside the constructors, and it's
    # value is available only in the instance/object.

    amount_01 = 10

    # A class constructor is a method that is automatically called when we
    # create objects of the class. If we do not define it explicitly, Python
    # will create it at run time and assign it to the object. the default constructor is created as follow:
    def __init__(self, parm_1, parm_2):  # __init__ is for constructor.
        # self is mandatory and indicate will contain the name of the object that
        # is currently instantiated/created for the class, and this is useful
        # to identify the instance/object variables defined in the constructor,
        # because "self" become part of the instance variable name:

        self.variable_1 = parm_1   # instance/object variable
        self.variable_2 = parm_2
        self.hector_instance_variable = 250.00

        print("**This constructor Method is called automatically when object is created ***")

    # all code starting in this line belong to the class
    def add(self):  # this method does not have parameters because it will
        # use the instance variable defined in the constructor.
        return self.variable_1 + self.variable_2 + HectorCalculator.acc_balance

    def multiply(self):
        return self.variable_1 * self.variable_2

    @staticmethod
    def greet():
        print("Good Morning")

    def global_acc_balance_hector(self):  # using global/class variable
        print("Object: ", self, "balance: ", HectorCalculator.acc_balance)
    # Hector_calculator.acc_balance and self.acc_balance contains the
    # same value from the class variable, because the "self" has access to
    # the instance and class variable content by inheritance.


# all the code starting here are outside the class definition.
def main():
    greet_hector()                # calling/using other methods defined in the script and outside the class defined
    greet_any_person("John Doe")
    greet_any_person("Carlos")
    add_integers(2, 5)
    value = add_int_return(10, 36)
    print("value: ", value)

    # now using the class defined:
    # in Python we instantiate/create objects of the class by assigning the class to
    # a variable outside the code range of the class definition, this is:
    object_calc = HectorCalculator(10, 45)  # the parameter are defined in the
    # constructor and passed once when instantiating/creating the object

    # to use the method in the class, we use the created object variable:
    object_calc.greet()
    print("HectorCalculator global variable acc_balance is: ", object_calc.acc_balance)
    print("using add(a,b) method:", object_calc.add())

    charge = object_calc.multiply()
    print("charge: ", charge)

    # Instantiating another object of the Hector_calculator class.
    obj099 = HectorCalculator(3, 12)
    print("second object add:", obj099.add())
    print("second object charge: ", obj099.multiply())
    obj099.greet()
    obj099.global_acc_balance_hector()


# program logic start here:
if __name__ == "__main__":  # program running from a submission of it self?
    main()   # Execute the main method; Not executed when the class defined in it is called or
             # inherited from another program using the class constructor method.
