# this program and the other (P10Use__name__varMainProg.py) are use to show show you how we can make use of
# the "__name__" variable to create modules in Python.
# Why is the __name__ variable used?
# The __name__ variable (two underscores before and after) is a special Python variable. It
# gets its value depending on how we execute the containing script.
# Sometimes we write a script with functions that might be useful in other scripts as well. In
# Python, we can import that script as a module in another calling/main/script.
# Thanks to this special variable, we can decide whether we want to run whole the script, Or only
# import the functions defined in the script.
#
# What values can the __name__ variable contain?
# When we run any script by itself (Not called/imported), the __name__ variable is initialized to the value "__main__".
# When the script is run by another calling program, the __name__ variable is populated with it's own name, in
# this case P09Use__name__varUtilitiesProgs; because any script/program start execution the first step is to
# initialize the content of the __name__ variable with either:
#        1- the value "__main__" (run by itself)
#        2- the value of it's own name. (when called from another main/calling program/script)
# This program "P09Use__name__varUtilitiesProgs.py" can be executed by it self and also called by others
# calling/main programs to use the functions defined in it

def myfunction():
    print("02 - The value of variable __name__ is " + __name__)


def main():
    print("01 - from main() method: the value of variable __name__ is " + __name__)  # Expected __main__
    myfunction()  # Execute myFunction() method.
    print("Executing statement 03 in Main() method")
    print("Executing statement 04 in Main() method")
    # add any other statement needed by the program/script...

# below statement is very dangerous because it will be executed every time that this script is called by
# another program, to avoid it we have to move it to a method, so that it have to be called for execution:

print("00 - Entering the Utilities program: the value of variable __name__ is " + __name__)  # Expected __main__


if __name__ == "__main__":  # This IF control the execution of below codes ONLY when this program is running by
    # it self; not when it is executed from an importing or calling program. This allows the calling programs to
    # use the methods defined here but not to execute the below codes when this program is called/imported.
    main()  # Execute main() method.


# Below the process executed:
# 1- Before all other code is run, the __name__ variable is set to the value "__main__".
# 2- After that, the main and myFunction def statements are run.
# 3- Because the condition evaluates to true, the main() function is called.
# 4- This, in turn, calls myFunction(). This prints out the value "__main__".