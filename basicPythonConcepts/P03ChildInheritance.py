# this program introduce the concept of Inheritance.
# inheritance is acquiring properties (variables and methods) from a
# parent/another class.
from basicPythonConcepts.P02FunctionAndClassDefinition import HectorCalculator


class UseCalculator(HectorCalculator):  # HectorCalculator is the parent class
    # after providing the parent class name the system will ask to import
    # the class and automatically will insert line 4 from P02Func....
    amount2 = 100

    # Because we are Inheritance from a parent class, this will trigger the __init__ constructor method in
    # the parent class and because this method requires two parameters (parm_1 and parm_2), to avoid the error:
    # "TypeError: __init__() missing 2 required positional arguments: 'parm_1' and 'parm_2'" then we need to
    # create an __init__ constructor here and calling the one from the parent class with the parameters populated:


    def __init__(self):
        HectorCalculator.__init__(self, 10, 20)


    def getCompleteTotal(self):
        return UseCalculator.amount2 + self.amount_01 + self.add()
        # self.amount_01 is a class variable from parent HectorCalculator
        # self.add() is a method from parent HectorCalculator.
        # UseCalculator.amount2 is a class variable in this child program.


def main():
    # now, out of the class code range, using this created method. First instantiate it or create the object
    childObject = UseCalculator()  # instantiate
    grandTotal = childObject.getCompleteTotal()
    print("*** The great total is: ", grandTotal)


if __name__ == "__main__":
    main()