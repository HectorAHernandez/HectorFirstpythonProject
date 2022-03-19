# A class is a collection of objects. A class contains the blueprint or prototype from which the objects are
# created or instantiated. A class is a logical entity containing some attributes and methods.
# In Python:
# 1- classes are created using the keyword 'class'.
# 2- Attributes are the variables that belong to the class
# 3- Attributes are always public and can be accessed by using the (.) operator: Myclass.Myattribute.

# Object: an object is an entity that has states (asstributes) and behaviors (methods) associated with it.
# any single integer number or string is an object. components of an object:
# 1- State: it is represented by the attributes of an object, the state also reflects the properties of an object.
# 2- Behavior: it is represented by the methods of an object. the behavior also reflects the response of an object
#    to others objects.
# 3- Identity: it give a unique name to an object and anables one object to interact with other objects.
# example of creating an object: obj = Dog()  this will create an object of the class Dog.

# keywords used with class and object creation:
# The self: Each class method must have an extract parameter in the method definition, this is the 'self' parameter.
# When we call the method we do not give a value for this parameter, Python provides it automatically.
# if we have method that takes no parameters, we still have to provide the 'self' parameter in the method definition.
# 'self' is similar to the pointer in C++ and the 'this' in Java.
# when we call a method of an object with Myobject.method(argument1, argument2), Python convert it automatically into:
# MyClass.method(Myobject, argument1, argument2). this is the object's name replace the 'self' parameter.

# The Constructor or __init__() method: a class constructor method is automtically executed as soon as an object of a
# class is instantiated/created. The constructor method is useful to do any initialization that we need to do with the
# object.

# creating a class and object with class and instance attributes:
class Dog:
    attr1 = "mammal"   # class attribute.

    # instance attribute in the constructor method:
    def __init__(self, parm_name):
        self.name = parm_name  # instance attribute: self.name

# Driver code: Objects instantiation:
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing the 'attr1' class attribute:
print("Rodger ia a {}".format(Rodger.attr1))
# or
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attribute (name)
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))


# Creating class and object containing methods:
class Cat:
    # class attribute
    breed = "feline"

    # class constructor method:
    def __init__(self, parm_name):
        self.name = parm_name  # instance attribute.

    def speak(self):
        print("My name is {}".format(self.name))

# object instantiation
Lucy = Cat("Lucy")
Lilly = Cat("Lilly")

# accessing class methods using the instantiated objects:
Lucy.speak()
Lilly.speak()
