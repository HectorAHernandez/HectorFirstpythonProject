# Inheritance is the capability of a class to inherit the properties of another class. The class deriving the
# properties is called the derived-class and the one from where the properties are derived is the called the
# Base-class or parent-class.
# benefits of inheritance:
# 1- it represent real world relationship.
# 2- it provides the re-usability of a code. No need to rewrite the same code again and again in the derived-class.
#    Also allows to to add more feature to a Base-class/Parent-class behaviour without modifying it. this is the
#    concept of expanding a Base-class by defining the a method in the chil-class with the same name as in the parent
#    class with the same functionalities and adding new ones. see the 'details()' method in the child-class below>
# 3- Transitivity: this means, if class-B inherits from class-A, then all others classes that inherit from class-B also
#    automatically inherit from class-A.

# below code demonstrates how the parent's constructor method is called from a child-class.
# parent class:
class Person(object):
    # __init_ constructor method:
    def __init__(self, parm_name, parm_id_num):
        self.name = parm_name
        self.id_number = parm_id_num

    def display(self):
        print("content of self.name {} ".format(self.name))
        print("content of self.id_number {} ".format(self.id_number))

    def details(self):
        print("My name is {}".format(self.name))
        print("My id Number is {}".format(self.id_number))


# child class Employee:
class Employee(Person):
    def __init__(self, parm_name, parm_my_id, parm_salary, parm_post):  # Employee class constructor method.
        self.salary = parm_salary
        self.post = parm_post

        # when a parent constructor method contains parameters, then the child class's constructor method always has
        # to invoke the parent constructor method providing the required parameters, this avoid error.
        Person.__init__(self, parm_name, parm_my_id)

    def details(self):
        print("My name is {} ".format(self.name))
        print("My id Number is {}".format(self.id_number))
        print("Expanded details method adding Post {}".format(self.post))
        print("More expansion, my Salary is {}".format(self.salary))

    def say_good_bye(self):
        print("**** Good bye all ")

    # notes: this child-class does not contains the display() method so, it is going to inherit it from the parent one.
    #        also, it is expanding the details() method from the parent and adding a new say_good_bye() method.


# Driver code: instantiating an object of the child-class:
empl = Employee("Hector", "820703", "50000000", "Good Post")

# calling a method of the Parent class (Person) using the just instantiated object of the child-class Employee:
empl.display()
# calling the expanded method details()
empl.details()
# calling the child-class created method say_good_bye():
empl.say_good_bye()


# next program is for Polymorphism in url: https://www.geeksforgeeks.org/python-oops-concepts/?ref=lbp