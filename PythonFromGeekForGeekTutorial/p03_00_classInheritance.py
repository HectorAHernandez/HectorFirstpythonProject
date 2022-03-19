# Inheritanc is a way in which a particular class inherits features (methods and attributes) from a BaseClass
# The BaseClass is also known as SuperClass and the class which inherites from the SuperClass is known as SubClass.
#   Base Class      SubClass
#   ----------      ---------
#   Feature1        Feature1
#   Feature2        Feature2
#   Feature3        Feature3
#                   Feature4

# The SubClass can inherit from the BaseClass and also can define its own Features
# The format to inherit from a BaseClass is:
#   class SubClass_name(BaseClass_name):

# Defining the BaseClass Pet:
class Pet:
    # __init__ is a constructor in Python:
    def __init__(self, parm_name, parm_age):
        self.name = parm_name
        self.age = parm_age

# Defining the SubClass Cat:
class Cat(Pet):
    # Defining the SubClass constructor, this is needed to explicitly call the BaseClass constructor with parameters
    # needed by the BaseClass. (if not created, the constructor will be failing with error because of missing parameters
    # if no parameters needed by the BaseClass then this call to the constructor method is not needed.
    def __init__(self, parm_name, parm_age):
        # calling the BaseClass constructor using the 'Super()' function:
        super().__init__(parm_name, parm_age)

def main():
    the_pet = Pet("Lizard", 1)    # create multiple pets/objects
    kitty1 = Cat("Lucy", 3)
    jess = Cat("jess", 100)
    kitty2 = Cat("Donnaa", 5)
    other_pet = Pet("Snakysty", 4)

    # To check whether an instantiated/creted object belong to the BaseClass or to the SubClass we
    # can use the 'isinstance(object_name, Class_name) function, which return True or False':
    print("Is Kitty1 a cat? " + str(isinstance(kitty1, Cat)))
    print("Is Kitty1 a Pet: " + str(isinstance(kitty1, Pet)))
    print("Is other_pet a cat? " + str(isinstance(other_pet, Cat)))
    print("What is the name of the other_pet? " + other_pet.name + " and age? " + str(other_pet.age))
    print("Is the pet a cat? " + str(isinstance(the_pet, Cat)))

# to let the Python program knows that there is a main() function:
if __name__ == "__main__":
    main()
